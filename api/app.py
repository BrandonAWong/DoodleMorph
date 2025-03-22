import torch
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
from datetime import datetime
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from huggingface_hub import login
from transformers import AutoModelForCausalLM, AutoProcessor
from dotenv import load_dotenv 
from os import getenv
from threading import Lock
from image import db, Image
import base64



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///images.db"
queue_lock = Lock()
db.init_app(app)
with app.app_context():
    db.create_all()
load_dotenv()
login(token=getenv("TOKEN"))

@app.route("/image", methods=["POST"])
def generate_image():
    data = request.get_json()
    doodle = data.get("doodle")
    style = data.get("style")
    with queue_lock:
        image_path = "test11.png"
        prompt = describe_image(image_path) + ", detailed, 4k, colorful, complex background, realistic"
        negative_prompt = "art, painting, drawing, artistry, render, nsfw, drawn, black and white, explicit"
        print(prompt)
        init_img = Image.open(image_path).convert("RGB")
        init_img = init_img.resize((768, 512))  # Adjust size as needed

        pipe = StableDiffusionImg2ImgPipeline.from_pretrained("SimianLuo/LCM_Dreamshaper_v7", torch_dtype=torch.float32)
        pipe = pipe.to("cuda")

        # if reailstic, up the strength to 60-65ish range and guidance to 7.5
        # if wana match the drawing. 50 is perfect and guidance to 4
        # pixelated ^

        result = pipe(prompt=prompt,
                      negative_prompt=negative_prompt,
                      image=init_img,
                      num_inference_steps=50,
                      strength=0.50,  # How much to transform the image (0-1)
                      guidance_scale=4.0)  # How closely to follow the prompt

        filename = f"./static/{datetime.now()}.png"
        result.images[0].save(filename)
        torch.cuda.empty_cache()
        generated = base64.b64encode(result.images[0]).decode('utf-8')
        new_image = Image(doodle=doodle, generated=generated, creationdate=datetime.now())
        db.session.add(new_image)
        db.session.commit()
        return f'<img src="{filename}">'

def describe_image(image_path):
    model_id = "microsoft/Florence-2-base"
    prompt = "<CAPTION>"

    model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
    model = model.to("cuda")
    processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)

    image = Image.open(image_path).convert("RGB")
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
        .replace("the image shows", "")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6521)

