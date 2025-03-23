<script setup lang="ts">
import SmartTransition from '@/components/smart/SmartTransition.vue';
import { watch } from 'vue';
import LoadingIndicator from '@/components/LoadingIndicator.vue';

const props = withDefaults(
  defineProps<{
    loading: boolean;
  }>(),
  {
    loading: false,
  },
);

watch(
  () => props.loading,
  (newValue) => {
    document.body.style.overflow = newValue ? 'hidden' : 'visible';
  },
);
</script>

<template>
  <Teleport to="body">
    <SmartTransition name="fade">
      <div v-if="loading" class="fixed inset-0 z-50 bg-[#E5E6F3]/[.7] text-center backdrop:blur-sm">
        <LoadingIndicator />
      </div>
    </SmartTransition>
  </Teleport>
</template>
