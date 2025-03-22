<script setup lang="ts">
import SketchCanvas from '@/components/SketchCanvas.vue';
import SmartSvg from '@/components/smart/SmartSvg.vue';
import { ref } from 'vue';

const base64 = ref('');
const lineWidth = ref(5);
const imageSrc = ref('');

async function generateImage() {
  const res = await fetch('http://45.49.181.126:6521/image', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      doodle: base64.value,
      style: 'Realistic',
    }),
  });

  console.log('res', res);

  const data = await res.json();

  imageSrc.value = data.image;
}
</script>

<template>
  <main class="font-notebook py-10 text-3xl">
    <h1 class="font-rock text-primary pb-20 text-center text-8xl font-bold">Doodle Morph</h1>
    <div class="mx-auto flex max-w-[1080px] justify-between">
      <div class="flex items-center">
        <div class="dropdown">
          <div tabindex="0" role="button" class="cursor-pointer">
            <SmartSvg src="pencil" class="h-14 w-14" />
          </div>
          <ul
            tabindex="0"
            class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm"
          >
            <li><a>Item 1</a></li>
            <li><a>Item 2</a></li>
          </ul>
        </div>

        <div class="dropdown">
          <div tabindex="0" role="button" class="cursor-pointer">
            <SmartSvg src="eraser" class="h-15 w-15" />
          </div>
          <ul
            tabindex="0"
            class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm"
          >
            <li><a>Item 1</a></li>
            <li><a>Item 2</a></li>
          </ul>
        </div>

        <div class="dropdown">
          <div tabindex="0" role="button" class="cursor-pointer">
            <SmartSvg src="bucket" class="h-16 w-16" />
          </div>
          <ul
            tabindex="0"
            class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm"
          >
            <li><a>Item 1</a></li>
            <li><a>Item 2</a></li>
          </ul>
        </div>

        <div class="dropdown ms-1">
          <div tabindex="0" role="button" class="cursor-pointer">
            <SmartSvg src="bars" class="h-14 w-14" />
          </div>
          <ul
            tabindex="0"
            class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm"
          >
            <li><button type="button" @click="lineWidth = 5">Line Width 5px</button></li>
            <li><button type="button" @click="lineWidth = 5">Line Width 10px</button></li>
            <li><button type="button" @click="lineWidth = 5">Line Width 15px</button></li>
            <li><button type="button" @click="lineWidth = 5">Line Width 20px</button></li>
          </ul>
        </div>

        <div>
          <input type="color" />
        </div>
      </div>
      <div class="flex items-center gap-2">
        <div class="dropdown dropdown-end">
          <div tabindex="0" role="button" class="btn btn-lg px-8 text-3xl">Select Theme</div>
          <ul
            tabindex="0"
            class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-sm"
          >
            <li><a>Realistic</a></li>
            <li><a>Pixilated</a></li>
            <li><a>Cartoon</a></li>
            <li><a>Anime</a></li>
          </ul>
        </div>
        <RouterLink to="/gallery">
          <SmartSvg src="gallery" class="h-14 w-14" />
        </RouterLink>
      </div>
    </div>
    <div class="flex items-center justify-center">
      <SketchCanvas
        v-model="base64"
        class="rounded border-6"
        :width="1080"
        :height="720"
        stroke-style="red"
        :line-width="lineWidth"
      />
    </div>

    <div class="mx-auto flex max-w-[1080px] justify-between py-2">
      <div class="flex items-center gap-2">
        <button class="btn btn-lg btn-secondary px-10">CLEAR</button>
        <SmartSvg src="undo-left" class="btn btn-lg" />
        <SmartSvg src="undo-right" class="btn btn-lg" />
      </div>
      <div>
        <button class="btn btn-lg btn-primary px-10" type="button" @click="generateImage">
          GENERATE
        </button>
      </div>
    </div>
    <div>
      <img :src="imageSrc" />
    </div>
  </main>
</template>
