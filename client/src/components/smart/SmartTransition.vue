<script setup lang="ts">
import { computed } from 'vue';

const props = withDefaults(
  defineProps<{
    name: string;
    mode?: 'in-out' | 'out-in' | 'default';
    duration?: number;
  }>(),
  { name: 'fade', duration: 300 },
);

const durationMS = computed(() => `${props.duration}ms`);
</script>

<template>
  <Transition :name="name" :mode="mode">
    <!-- eslint-disable-next-line vue/require-toggle-inside-transition -->
    <slot />
  </Transition>
</template>

<style scoped lang="scss">
.fade {
  &-enter-from,
  &-leave-to {
    opacity: 0;
  }

  &-enter-active,
  &-leave-active {
    transition: all v-bind(durationMS) ease-in-out;
  }
}

.slide-from-right {
  &-enter-from,
  &-leave-to {
    transform: translateX(100%);
  }

  &-enter-active,
  &-leave-active {
    transition: all v-bind(durationMS) ease-in-out;
  }
}

.fade-up {
  &-enter-from,
  &-leave-to {
    transform: translateY(1%);
    opacity: 0;
  }

  &-enter-active,
  &-leave-active {
    transition: all v-bind(durationMS) ease;
  }
}
</style>
