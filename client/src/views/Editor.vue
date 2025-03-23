<script setup lang="ts">
import SketchCanvas from '@/components/SketchCanvas.vue';
import SmartSvg from '@/components/smart/SmartSvg.vue';
import { inject, ref, useTemplateRef } from 'vue';

const WIDTH = 1080;
const HEIGHT = 720;

const refMyCanvas = useTemplateRef('myCanvas');
const base64 = ref('');

const history = ref<(ImageData | undefined)[]>([]);
const redoHistory = ref<(ImageData | undefined)[]>([]);

const lineWidth = ref(5);
const imageSrc = ref('');
const theme = ref('Realistic');
const color = ref('#000000');
const mode = ref('Draw');

const startOverlay = inject('start-overlay', () => {});
const stopOverlay = inject('stop-overlay', () => {});

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
  try {
    startOverlay();

    const res = await fetch('http://45.49.181.126:6521/image', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        doodle: base64.value,
        style: theme.value,
      }),
    });

    const data = await res.json();

    imageSrc.value = data.image;
  } finally {
    stopOverlay();
  }
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
  const ctx = refMyCanvas.value?.ctxRef;

  if (!ctx) {
    return;
  }

  // Clear the canvas
  ctx.clearRect(0, 0, WIDTH, HEIGHT);
  // Fill canvas with white
  ctx.fillStyle = 'white';
  ctx.fillRect(0, 0, WIDTH, HEIGHT);
}

async function undo() {
  const ctx = refMyCanvas.value?.ctxRef;

  if (!ctx || history.value.length === 0) {
    return;
  }

  redoHistory.value.push(history.value.pop());

  const prevState = history.value[history.value.length - 1];

  if (prevState) {
    ctx.putImageData(prevState, 0, 0);
  } else {
    // kinda kinky but its ok
    clearCanvas();
    redoHistory.value = [];
  }
}

function redo() {
  const ctx = refMyCanvas.value?.ctxRef;

  if (!ctx || redoHistory.value.length === 0) {
    return;
  }

  const nextState = redoHistory.value.pop();

  if (nextState) {
    history.value.push(nextState);
    ctx.putImageData(nextState, 0, 0);
  }
}
</script>

<template>
  <main
    class="font-notebook bg-[#E5E6F3] bg-cover py-10 text-3xl"
    :style="{ backgroundImage: 'url(/images/background.png)' }"
  >
    <div class="pb-20 text-center">
      <RouterLink to="/" class="font-rock text-8xl font-bold text-[#394DA8]">
        Doodle Morph
      </RouterLink>
    </div>

    <div class="mx-auto flex max-w-[1080px] justify-between">
      <div class="flex items-center">
        <SmartSvg
          src="pencil"
          class="h-14 w-14 cursor-pointer"
          :class="{
            '-translate-y-2 transition-all': mode === 'Draw',
          }"
          @click="mode = 'Draw'"
        />

        <SmartSvg
          src="eraser"
          class="h-15 w-15 cursor-pointer"
          :class="{
            '-translate-y-2 transition-all': mode === 'Erase',
          }"
          @click="mode = 'Erase'"
        />

        <SmartSvg
          src="bucket"
          class="h-16 w-16 cursor-pointer"
          :class="{
            '-translate-y-2 transition-all': mode === 'Bucket',
          }"
          @click="mode = 'Bucket'"
        />

        <div class="dropdown ms-1">
          <div tabindex="0" role="button" class="cursor-pointer">
            <SmartSvg src="bars" class="h-14 w-14" />
          </div>
          <ul
            tabindex="0"
            class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 text-3xl shadow-sm"
          >
            <li><button type="button" @click="lineWidth = 5">Line Width 5px</button></li>
            <li><button type="button" @click="lineWidth = 10">Line Width 10px</button></li>
            <li><button type="button" @click="lineWidth = 15">Line Width 15px</button></li>
            <li><button type="button" @click="lineWidth = 20">Line Width 20px</button></li>
          </ul>
        </div>

        <div class="ms-3 flex gap-2">
          <div
            class="h-10 w-10 cursor-pointer rounded-full border-3 border-[#394DA8] bg-[#000000]"
            @click="color = '#000000'"
          />
          <div
            class="h-10 w-10 cursor-pointer rounded-full border-3 border-[#394DA8] bg-[#CD1818]"
            @click="color = '#CD1818'"
          />
          <div
            class="h-10 w-10 cursor-pointer rounded-full border-3 border-[#394DA8] bg-[#18CD36]"
            @click="color = '#18CD36'"
          />
          <div
            class="h-10 w-10 cursor-pointer rounded-full border-3 border-[#394DA8] bg-[#1876CD]"
            @click="color = '#1876CD'"
          />
          <div
            class="h-10 w-10 cursor-pointer rounded-full border-3 border-[#394DA8] bg-[#6118CD]"
            @click="color = '#6118CD'"
          />
          <input v-model="color" class="h-10 w-10 cursor-pointer" type="color" />
        </div>
      </div>
      <div class="flex items-center gap-2">
        <div class="dropdown dropdown-end">
          <div tabindex="0" role="button" class="btn btn-lg px-8 text-3xl">{{ theme }}</div>
          <ul
            tabindex="0"
            class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 text-3xl shadow-sm"
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
        v-model:image="base64"
        v-model:state="history"
        class="rounded border-6"
        :width="WIDTH"
        :height="HEIGHT"
        :stroke-style="color"
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
        <SmartSvg
          src="undo-left"
          class="btn btn-lg"
          :class="{ 'btn-disabled': history.length === 0 }"
          @click="undo"
        />
        <SmartSvg
          src="undo-right"
          class="btn btn-lg"
          :class="{ 'btn-disabled': redoHistory.length === 0 }"
          @click="redo"
        />
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
