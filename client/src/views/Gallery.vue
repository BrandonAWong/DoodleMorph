<script setup lang="ts">
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
    <div class="flex h-screen flex-col items-center justify-center bg-[#E5E6F3] bg-cover bg-center"
      :style="{ backgroundImage: `url(${bgImage})` }"></div>

  </main>
</template>
