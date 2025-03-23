<script setup lang="ts">
import { provide, ref } from 'vue';
import SmartTransition from '@/components/smart/SmartTransition.vue';
import LoadingOverlay from './components/LoadingOverlay.vue';

const isLoading = ref(false);

provide('start-overlay', () => (isLoading.value = true));
provide('stop-overlay', () => (isLoading.value = false));
</script>

<template>
  <LoadingOverlay :loading="isLoading" />
  <RouterView v-slot="{ Component }" class="router-view">
    <SmartTransition name="fade-up" mode="out-in" :duration="500">
      <component :is="Component" />
    </SmartTransition>
  </RouterView>
</template>

<style scoped lang="scss">
.router-view {
  min-height: calc(100vh - 460px);
}
</style>
