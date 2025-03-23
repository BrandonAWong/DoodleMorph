<script setup lang="ts">
import SmartSvg from './smart/SmartSvg.vue';
</script>

<template>
  <div class="flex h-full w-full items-center justify-center">
    <SmartSvg
      src="loading"
      class="animate-spin fill-[#394DA8] stroke-[#394DA8]"
      width="75px"
      height="75px"
    />
  </div>
</template>
