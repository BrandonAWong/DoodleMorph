import torch
from diffusers import StableDiffusionImg2ImgPipeline
import PIL
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from sqlalchemy import desc
from huggingface_hub import login
from transformers import AutoModelForCausalLM, AutoProcessor
from dotenv import load_dotenv
from os import getenv
from threading import Lock
from image import db, Image
import base64
from io import BytesIO


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///images.db"
CORS(app)

db.init_app(app)
with app.app_context():
    db.create_all()

load_dotenv()
login(token=getenv("TOKEN"))

queue_lock = Lock()

@app.route("/image", methods=["POST"])
def generate_image():
    data = request.get_json()
    doodle_base64 = data.get("doodle")
    doodle = BytesIO(base64.b64decode(doodle_base64.replace("data:image/png;base64,", "")))
    style = data.get("style")

    with queue_lock:
        prompt = describe_image(doodle) + ", detailed, 4k, complex background, "
        strength = 0.5
        guidance = 4
        match (style.lower()):
            case "realistic":
                prompt += "realistic"
                strength = 0.60
                guidance = 7
            case "pixelated":
                prompt += "pixelated, pixel art"
            case "cartoonish":
                prompt += "cartoonish, cartoony"
            case "anime":
                strength = 0.60
                prompt += "anime"

        negative_prompt = "art, painting, drawing, artistry, render, nsfw, drawn, black and white, explicit"
        init_img = PIL.Image.open(doodle).convert("RGB")
        init_img = init_img.resize((768, 512))  # Adjust size as needed

        pipe = StableDiffusionImg2ImgPipeline.from_pretrained("SimianLuo/LCM_Dreamshaper_v7", torch_dtype=torch.float32)
        pipe = pipe.to("cuda")
        pipe.safety_checker = None

        result = pipe(prompt=prompt,
                      negative_prompt=negative_prompt,
                      image=init_img,
                      num_inference_steps=50,
                      strength=strength,
                      guidance_scale=guidance)

        torch.cuda.empty_cache()

        buffered = BytesIO()
        result.images[0].save(buffered, format="PNG")  # Save as PNG or any other format
        img_bytes = buffered.getvalue()
        generated = "data:image/png;base64," + base64.b64encode(img_bytes).decode('utf-8')

        new_image = Image(doodle=doodle_base64, generated=generated, creationdate=datetime.now())
        db.session.add(new_image)
        db.session.commit()
        print(prompt)
        return jsonify({"image": generated})

def describe_image(image_path):
    model_id = "microsoft/Florence-2-base"
    prompt = "<CAPTION>"

    model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
    model = model.to("cuda")
    processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)
    image = PIL.Image.open(image_path).convert("RGB")
    inputs = processor(text=prompt, images=image, return_tensors="pt").to("cuda", torch.float32)

    generated_ids = model.generate(
        input_ids=inputs["input_ids"],
        pixel_values=inputs["pixel_values"],
        max_new_tokens=1024,
        do_sample=False,
        num_beams=10,
    )

    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
    parsed_answer = processor.post_process_generation(generated_text, task=prompt, image_size=(image.width, image.height))
    torch.cuda.empty_cache()
    return parsed_answer[prompt].lower()\
        .replace("drawing", "picture")\
        .replace("black and white", "")\
        .replace("the image shows", "")\
        .replace("how to", "")\
        .replace("draw", "")\
        .replace(".", "")

@app.route("/image", methods=["GET"])
def get_gallery_images():
    offset = request.args.get('offset',0,type=int)
    limit = request.args.get('limit',5,type=int)
    images = Image.query.order_by(desc(Image.creationdate)).offset(offset).limit(limit).all()
    images_list = []
    for image in images:
        info = {"id": image.id, "doodle":image.doodle, "generated":image.generated, "creationdate":image.creationdate}
        images_list.append(info)
    return jsonify({"images": images_list})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6521)

