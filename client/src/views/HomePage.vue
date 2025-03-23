<script setup lang="ts">
import playIcon from '@/assets/playIcon.png';
import bgImage from '@/assets/bgImage.png';
import galleryIcon from '@/assets/galleryIcon.png';
</script>

<template>
  <main>
    <!-- This is for the gallery icon in the top right which links to the gallery page. -->
    <div class="absolute top-6 right-6">
      <RouterLink to="/gallery">
        <img
          :src="galleryIcon"
          alt="Gallery Icon"
          class="shrink-0 opacity-80 transition duration-200 hover:opacity-100"
        />
      </RouterLink>
    </div>

    <!-- This is for the home page title -->
    <div
      class="flex h-screen flex-col items-center justify-center bg-[#E5E6F3] bg-cover bg-center"
      :style="{ backgroundImage: `url(${bgImage})` }"
    >
      <div class="flex -translate-y-30 transform items-center justify-center text-9xl">
        <div class="font-rock h-[404px] w-[703px] shrink-0 p-35 font-bold text-[#394DA8]"">
          Doodle Morph
        </div>
      </div>

      <!-- Play button below the title -->
      <div class="flex transform justify-center pt-10">
        <RouterLink to="/editor">
          <img
            :src="playIcon"
            alt="Editor Icon"
            class="w-176.174px h-174.306px shrink-0 p-20 opacity-80 transition duration-200 hover:opacity-100"
          />
        </RouterLink>
      </div>
    </div>
  </main>
</template>
