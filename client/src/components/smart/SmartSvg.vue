<script setup lang="ts">
import { log } from '@/assets/utility';
import { computed, defineAsyncComponent } from 'vue';

const SVGS = import.meta.glob('@/assets/svgs/**/*.svg') as Record<
  string,
  () => Promise<{ default: unknown }>
>;

const props = defineProps({
  src: {
    type: String,
    required: true,
  },
});

const derivedComponent = computed(() => {
  try {
    const component = SVGS[`/src/assets/svgs/${props.src}.svg`]();
    return defineAsyncComponent(() => component);
  } catch {
    log(`Error: svg ${props.src} not found.`);
  }

  return null;
});
</script>

<template>
  <component :is="derivedComponent" />
</template>
