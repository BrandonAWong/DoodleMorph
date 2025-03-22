<script setup lang="ts">
import { onMounted, ref, useTemplateRef } from 'vue';

defineProps<{
  width: number;
  height: number;
}>();

const canvas = useTemplateRef('myCanvas');

const isDrawing = ref(false);

let ctx: CanvasRenderingContext2D | null = null;

function initCtx() {
  if (!canvas.value) {
    return;
  }

  ctx = canvas.value.getContext('2d');

  ctx?.strokeStyle = 'blue';
  ctx?.lineWidth = 3;
  ctx?.lineCap = 'round';

  canvas.value.addEventListener('mousedown', (e) => {
    isDrawing.value = true;
    ctx?.beginPath();
    ctx?.moveTo(e.offsetX, e.offsetY);
  });

  canvas.value.addEventListener('mousemove', (e) => {
    if (!isDrawing.value) {
      return;
    }

    ctx?.lineTo(e.offsetX, e.offsetY);
    ctx?.stroke();
  });

  canvas.value.addEventListener('mouseup', async () => {
    isDrawing.value = false;
    const image = canvas.value?.toDataURL();
    console.log(image);
  });
}

onMounted(() => {
  initCtx();
});
</script>

<template>
  <canvas ref="myCanvas" :width="width" :height="height"></canvas>
</template>
