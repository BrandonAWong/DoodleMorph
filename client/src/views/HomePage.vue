<script setup lang="ts">
import editorIcon from '@/assets/playButton.png';
import bgImage from '@/assets/background.png';
import galleryIcon from '@/assets/galleryButton.png';
</script>

<template>
  <main>
    <!-- <div class="absolute top-6 right-6">
      <button class="bg-red-500 text-white px-4 py-2 rounded hover:bg-blue-700 transition">
        Top Right
      </button>
    </div> -->

    <div class="absolute top-6 right-6">
      <RouterLink to="/editor">
        <img
          :src="galleryIcon"
          alt="Gallery Icon"
          class="shrink-0 opacity-80 transition duration-200 hover:opacity-100"
        />
      </RouterLink>
    </div>

    <div
      class="flex h-screen flex-col items-center justify-center bg-[#E5E6F3] bg-cover bg-center"
      :style="{ backgroundImage: `url(${bgImage})` }"
    >
      <div class="flex -translate-y-30 transform items-center justify-center text-9xl">
        <div class="font-rock h-[404px] w-[703px] shrink-0 p-35 font-bold text-[#394DA8]">
          Doodle Morph
        </div>
      </div>

      <div class="flex transform justify-center pt-10">
        <RouterLink to="/editor">
          <img
            :src="editorIcon"
            alt="Editor Icon"
            class="w-176.174px h-174.306px shrink-0 p-20 opacity-80 transition duration-200 hover:opacity-100"
          />
        </RouterLink>
      </div>
    </div>
  </main>
</template>
