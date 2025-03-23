<script setup lang="ts">
import SketchCanvas from '@/components/SketchCanvas.vue';
import SmartSvg from '@/components/smart/SmartSvg.vue';
import bgImage from '@/assets/bgImage.png';
import { ref, useTemplateRef } from 'vue';

const WIDTH = 1080;
const HEIGHT = 720;

const refMyCanvas = useTemplateRef('myCanvas');
const base64 = ref('');
const lineWidth = ref(5);
const imageSrc = ref('');
const theme = ref('Realistic');

/**
 * POST doodle and style to server, and set imageSrc to the response.
 *
 * @remarks
 * This function is used to generate an image based on the doodle and style.
 * The doodle is the base64 representation of the canvas.
 * The style is the theme selected by the user.
 * The response from the server is in JSON format, and the image is stored in the
 * `image` property of the response.
 */
async function generateImage() {
  const res = await fetch('http://45.49.181.126:6521/image', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      doodle: base64.value,
      style: theme.value,
    }),
  });

  console.log('res', res);

  const data = await res.json();

  imageSrc.value = data.image;
}

/**
 * Clears the entire canvas by resetting it to a blank white state.
 *
 * @remarks
 * This function accesses the 2D rendering context of the canvas and performs
 * a clear operation over the entire area specified by WIDTH and HEIGHT.
 * It then fills the canvas with a white rectangle to ensure a clean slate
 * for further drawing operations.
 *
 * @function clearCanvas
 */
function clearCanvas() {
  const context = refMyCanvas.value?.ctxRef;

  if (!context) return;
  // Clear the canvas
  context.clearRect(0, 0, WIDTH, HEIGHT);
  // Fill canvas with white
  context.fillStyle = 'white';
  context.fillRect(0, 0, WIDTH, HEIGHT);
}
</script>

<template>
  <!-- <div class="flex h-screen flex-col items-center justify-center bg-[#E5E6F3] bg-cover bg-center"
     :style="{ backgroundImage: `url(${bgImage})` }"></div> -->

  <main
    class="font-notebook bg-[#E5E6F3] bg-cover py-10 text-3xl"
    :style="{ backgroundImage: `url(${bgImage})` }"
  >
    <h1 class="font-rock pb-20 text-center text-8xl font-bold text-[#394DA8]">Doodle Morph</h1>
    <div class="mx-auto flex max-w-[1080px] justify-between">
      <div class="flex items-center">
        <SmartSvg src="pencil" class="h-14 w-14 cursor-pointer" />

        <SmartSvg src="eraser" class="h-15 w-15 cursor-pointer" />

        <SmartSvg src="bucket" class="h-16 w-16 cursor-pointer" />

        <div class="dropdown ms-1">
          <div tabindex="0" role="button" class="cursor-pointer">
            <SmartSvg src="bars" class="h-14 w-14" />
          </div>
          <ul
            tabindex="0"
            class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 text-2xl shadow-sm"
          >
            <li><button type="button" @click="lineWidth = 5">Line Width 5px</button></li>
            <li><button type="button" @click="lineWidth = 10">Line Width 10px</button></li>
            <li><button type="button" @click="lineWidth = 15">Line Width 15px</button></li>
            <li><button type="button" @click="lineWidth = 20">Line Width 20px</button></li>
          </ul>
        </div>

        <div>
          <input type="color" />
        </div>
      </div>
      <div class="flex items-center gap-2">
        <div class="dropdown dropdown-end">
          <div tabindex="0" role="button" class="btn btn-lg px-8 text-3xl">{{ theme }}</div>
          <ul
            tabindex="0"
            class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 text-2xl shadow-sm"
          >
            <li><button type="button" @click="theme = 'Realistic'">Realistic</button></li>
            <li><button type="button" @click="theme = 'Pixelated'">Pixelated</button></li>
            <li><button type="button" @click="theme = 'Cartoon'">Cartoon</button></li>
            <li><button type="button" @click="theme = 'Anime'">Anime</button></li>
          </ul>
        </div>
        <RouterLink to="/gallery">
          <SmartSvg src="gallery" class="h-14 w-14" />
        </RouterLink>
      </div>
    </div>
    <div class="flex items-center justify-center">
      <SketchCanvas
        ref="myCanvas"
        v-model="base64"
        class="rounded border-6"
        :width="WIDTH"
        :height="HEIGHT"
        stroke-style="black"
        :line-width="lineWidth"
      />
    </div>

    <div class="mx-auto flex max-w-[1080px] justify-between py-2">
      <div class="flex items-center gap-2">
        <button
          class="btn btn-lg btn-secondary border-[#394DA8] bg-[#E5E6F3] px-10 text-[#394DA8]"
          type="button"
          @click="clearCanvas"
        >
          clear
        </button>
        <SmartSvg src="undo-left" class="btn btn-lg" />
        <SmartSvg src="undo-right" class="btn btn-lg" />
      </div>
      <div>
        <button
          class="btn btn-lg btn-primary border-[#394DA8] bg-[#E5E6F3] px-10 text-[#394DA8]"
          type="button"
          @click="generateImage"
        >
          generate
        </button>
      </div>
    </div>
    <div class="flex justify-center py-10">
      <img :src="imageSrc" />
    </div>
  </main>
</template>
