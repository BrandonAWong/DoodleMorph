<script setup lang="ts">
import { onMounted, ref, useTemplateRef, watch } from 'vue';

const props = defineProps<{
  width: number;
  height: number;
  strokeStyle: string;
  lineWidth: number;
  mode: string;
}>();

const model = defineModel<string | undefined>('image', { required: true });
const state = defineModel<(ImageData | undefined)[]>('state', { default: () => [] });

const canvas = useTemplateRef('myCanvas');

const isDrawing = ref(false);

const ctxRef = ref<CanvasRenderingContext2D | null>(null);

function initCtx() {
  if (!canvas.value) {
    return;
  }

  ctxRef.value = canvas.value.getContext('2d', { willReadFrequently: true });

  if (!ctxRef.value) {
    return;
  }

  ctxRef.value.strokeStyle = props.strokeStyle;
  ctxRef.value.lineWidth = props.lineWidth;
  ctxRef.value.fillStyle = 'white';
  ctxRef.value.fillRect(0, 0, props.width, props.height);

  canvas.value.addEventListener('mousedown', (e) => {
    isDrawing.value = true;
    ctxRef.value?.beginPath();
    ctxRef.value?.moveTo(e.offsetX, e.offsetY);
  });

  canvas.value.addEventListener('mousemove', (e) => {
    if (!isDrawing.value) return;

    if (!ctxRef.value) return;

    if (props.mode == 'Erase') {
      ctxRef.value.strokeStyle = 'white';
    } else {
      ctxRef.value.strokeStyle = props.strokeStyle;
    }
    ctxRef.value?.lineTo(e.offsetX, e.offsetY);
    ctxRef.value?.stroke();
  });

  canvas.value.addEventListener('mouseup', async () => {
    isDrawing.value = false;
    model.value = canvas.value?.toDataURL();
    const binImage = ctxRef.value?.getImageData(0, 0, props.width, props.height);
    state.value.push(binImage);
  });
}

watch(
  () => [props.strokeStyle, props.lineWidth, props.mode],
  () => {
    if (!ctxRef.value) return;

    ctxRef.value.lineWidth = props.lineWidth;
    
    if (props.mode == 'Erase') {
      ctxRef.value.strokeStyle = 'white';
    } else {
      ctxRef.value.strokeStyle = props.strokeStyle;
    }
  },
);

onMounted(() => {
  initCtx();
});

defineExpose({
  ctxRef,
});
</script>

<template>
  <canvas
    ref="myCanvas"
    :width="width"
    :height="height"
    class="rounded-xl border-4 border-[#394DA8]"
  ></canvas>
</template>
