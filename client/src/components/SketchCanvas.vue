<script setup lang="ts">
import { onMounted, ref, useTemplateRef, watch } from 'vue';

const props = defineProps<{
  width: number;
  height: number;
  strokeStyle: string;
  lineWidth: number;
}>();

const model = defineModel<string | undefined>({ required: true });

const canvas = useTemplateRef('myCanvas');

const isDrawing = ref(false);

let ctx: CanvasRenderingContext2D | null = null;

function initCtx() {
  if (!canvas.value) {
    return;
  }

  ctx = canvas.value.getContext('2d');

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
    model.value = canvas.value?.toDataURL();
  });
}

watch(
  props,
  ({ strokeStyle, lineWidth }) => {
    if (!ctx) {
      return;
    }

    ctx.strokeStyle = strokeStyle;
    ctx.lineWidth = lineWidth;
  },
  { immediate: true },
);

onMounted(() => {
  initCtx();
});
</script>

<template>
  <canvas ref="myCanvas" :width="width" :height="height"></canvas>
</template>
