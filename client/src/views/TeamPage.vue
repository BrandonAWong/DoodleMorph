<script setup lang="ts">
import SmartSvg from '@/components/smart/SmartSvg.vue';
</script>

<template>
  <main
    class="bg-[#E5E6F3] bg-cover bg-center"
    :style="{ backgroundImage: 'url(/images/background.png)' }"
  >
  <div class="flex -translate-y-30 transform items-center justify-center text-8xl mb-0">
        <div class="font-rock h-[200px] w-[800px] shrink-0 pt-35 pl-35 mb-0 font-bold text-[#394DA8] tracking-tighter short-spaces">
          Our Team
        </div>
  </div>

  <div class="flex justify-center gap-35 text-[#394DA8] font-notebook font-semibold text-[34px]">

    <div class="flex flex-col items-center w-[364px] h-[368px] bg-white text-center rounded-[18px] border-[#394DA8] border-5">
      <div class="relative -top-5 w-[228px] h-[52px] rounded-[18px] border-[#394DA8] border-5 bg-white">
        Brandon Wong
      </div>
      <SmartSvg
          src="brandon"
          class="relative zh-[212px] w-[212px] overflow-visible"
      />
      <div class="relative top-5 left-3 w-[367px] h-[118px] text-left rounded-[18px] border-[#394DA8] border-5 bg-white">
        <p class="ml-3">poopy muncher</p>
      </div>
    </div>

    <div class="flex flex-col items-center w-[364px] h-[368px] bg-white text-center rounded-[18px] border-[#394DA8] border-5">
      <div class="relative -top-5 w-[228px] h-[52px] rounded-[18px] border-[#394DA8] border-5 bg-white">
        Kaveh Zare
      </div>
      <SmartSvg
          src="kaveh"
          class="relative zh-[212px] w-[212px] overflow-visible"
        />
      <div class="relative top-5 left-3 w-[367px] h-[118px] text-left rounded-[18px] border-[#394DA8] border-5 bg-white">
        <p class="ml-3">dicsord mod</p>
      </div>
    </div>
  </div>

  <div class="flex justify-center gap-35 text-[#394DA8] font-notebook font-semibold text-[34px] mt-20">

<div class="flex flex-col items-center w-[364px] h-[368px] bg-white text-center rounded-[18px] border-[#394DA8] border-5">
  <div class="relative -top-5 w-[228px] h-[52px] rounded-[18px] border-[#394DA8] border-5 bg-white">
    Sophia Doan
  </div>
  <SmartSvg
      src="sophia"
      class="relative zh-[212px] w-[212px] overflow-visible"
    />
  <div class="relative top-5 left-3 w-[367px] h-[118px] text-left rounded-[18px] border-[#394DA8] border-5 bg-white">
    <p class="ml-3">butt booty naked men enjoyer</p>
  </div>
</div>

<div class="flex flex-col items-center w-[364px] h-[368px] bg-white text-center rounded-[18px] border-[#394DA8] border-5">
  <div class="relative -top-5 w-[228px] h-[52px] rounded-[18px] border-[#394DA8] border-5 bg-white">
    Carlos Aguilera
  </div>
  <SmartSvg
      src="carlos"
      class="relative zh-[212px] w-[212px] overflow-visible"
    />
  <div class="relative top-5 left-3 w-[367px] h-[118px] text-left rounded-[18px] border-[#394DA8] border-5 bg-white">
    <p class="ml-3">diversity hire</p>
  </div>
</div>
</div>

  </main>
</template>

<style>
  .short-spaces {
    word-spacing: -60px;
  }
</style>