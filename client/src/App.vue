<script setup lang="ts">
import { provide, ref } from 'vue';
import SmartTransition from '@/components/smart/SmartTransition.vue';
import LoadingOverlay from './components/LoadingOverlay.vue';

const isLoading = ref(false);

provide('start-overlay', () => (isLoading.value = true));
provide('stop-overlay', () => (isLoading.value = false));
</script>

<template>
  <div>
    <LoadingOverlay :loading="isLoading" />

    <RouterView v-slot="{ Component }">
      <SmartTransition name="fade-up" mode="out-in">
        <component :is="Component" />
      </SmartTransition>
    </RouterView>
  </div>
</template>
