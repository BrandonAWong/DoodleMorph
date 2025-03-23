<script setup lang="ts">
import SmartSvg from '@/components/smart/SmartSvg.vue';
</script>

<template>
  <main
    class="h-screen bg-[#E5E6F3] bg-cover bg-center"
    :style="{ backgroundImage: 'url(/images/background.png)' }"
  >
    <!-- This is for the gallery icon in the top right which links to the gallery page. -->
    <div class="absolute top-6 right-6">
      <RouterLink to="/gallery">
        <SmartSvg
          src="gallery"
          class="shrink-0 opacity-80 transition duration-200 hover:opacity-100"
        />
      </RouterLink>
    </div>
  </main>
</template>
