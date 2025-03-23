<script setup lang="ts">
import SmartSvg from '@/components/smart/SmartSvg.vue';
</script>

<template>
  <main
    class="relative h-screen bg-[#E5E6F3] bg-cover bg-center"
    :style="{ backgroundImage: 'url(/images/background.png)' }"
  >
    <!-- This is for the gallery icon in the top right which links to the gallery page. -->
    <div class="absolute top-6 left-6 z-10">
      <RouterLink to="/">
        <SmartSvg
          src="undo-left"
          class="h-16 w-16 shrink-0 opacity-100 transition duration-200 hover:opacity-80"
        />
      </RouterLink>
    </div>

    <div class="mb-0 flex -translate-y-30 text-8xl">
      <div
        class="font-rock short-spaces h-[200px] w-[100%] shrink-0 pt-35 text-center font-bold tracking-tighter text-[#394DA8]"
      >
        Gallery
      </div>
    </div>
  </main>
</template>
