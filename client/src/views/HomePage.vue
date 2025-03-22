<script setup lang="ts">
import SketchCanvas from '@/components/SketchCanvas.vue';
</script>

<template>
  <main>
    <button class="max-w-2 bg-blue-500 hover:bg-amber-50">My Button</button>
    <div class="flex items-center justify-center">
      <SketchCanvas class="border-3" :width="1080" :height="720" />
    </div>
  </main>
</template>
