<script setup lang="ts">
import SmartSvg from '@/components/smart/SmartSvg.vue';
</script>

<template>
  <main
    class="bg-[#E5E6F3] bg-cover bg-center pb-14"
    :style="{ backgroundImage: 'url(/images/background.png)' }"
  >
    <div class="absolute top-6 left-6 z-10">
      <RouterLink to="/">
        <SmartSvg
          src="undo-left"
          class="h-16 w-16 shrink-0 opacity-100 transition duration-200 hover:opacity-80"
        />
      </RouterLink>
    </div>

    <div class="mb-0 flex -translate-y-30 text-8xl">
      <div
        class="font-rock short-spaces h-[200px] w-[100%] shrink-0 pt-35 text-center font-bold tracking-tighter text-[#394DA8]"
      >
        Our Team
      </div>
    </div>

    <div class="font-notebook flex justify-center gap-35 text-[34px] font-semibold text-[#394DA8]">
      <div
        class="flex h-[368px] w-[364px] flex-col items-center rounded-[18px] border-5 border-[#394DA8] bg-white text-center"
      >
        <div
          class="relative -top-5 h-[52px] w-[228px] rounded-[18px] border-5 border-[#394DA8] bg-white"
        >
          Brandon Wong
        </div>
        <img src="/src/assets/brandon.png" class="zh-[212px] relative w-[212px] overflow-visible" />
        <div
          class="relative top-5 left-3 h-[118px] w-[367px] rounded-[18px] border-5 border-[#394DA8] bg-white text-left"
        >
          <p class="ml-3">poopy muncher</p>
        </div>
      </div>

      <div
        class="flex h-[368px] w-[364px] flex-col items-center rounded-[18px] border-5 border-[#394DA8] bg-white text-center"
      >
        <div
          class="relative -top-5 h-[52px] w-[228px] rounded-[18px] border-5 border-[#394DA8] bg-white"
        >
          Kaveh Zare
        </div>
        <img src="/src/assets/kaveh.png" class="zh-[212px] relative w-[212px] overflow-visible" />
        <div
          class="relative top-5 left-3 h-[118px] w-[367px] rounded-[18px] border-5 border-[#394DA8] bg-white text-left"
        >
          <p class="ml-3">discord mod</p>
        </div>
      </div>
    </div>

    <div
      class="font-notebook mt-20 flex justify-center gap-35 text-[34px] font-semibold text-[#394DA8]"
    >
      <div
        class="flex h-[368px] w-[364px] flex-col items-center rounded-[18px] border-5 border-[#394DA8] bg-white text-center"
      >
        <div
          class="relative -top-5 h-[52px] w-[228px] rounded-[18px] border-5 border-[#394DA8] bg-white"
        >
          Sophia Doan
        </div>
        <img src="/src/assets/sophia.png" class="zh-[212px] relative w-[212px] overflow-visible" />
        <div
          class="relative top-5 left-3 h-[118px] w-[367px] rounded-[18px] border-5 border-[#394DA8] bg-white text-left"
        >
          <p class="ml-3">butt booty naked men enjoyer</p>
        </div>
      </div>

      <div
        class="flex h-[368px] w-[364px] flex-col items-center rounded-[18px] border-5 border-[#394DA8] bg-white text-center"
      >
        <div
          class="relative -top-5 h-[52px] w-[228px] rounded-[18px] border-5 border-[#394DA8] bg-white"
        >
          Carlos Aguilera
        </div>
        <img src="/src/assets/carlos.png" class="zh-[212px] relative w-[212px] overflow-visible" />
        <div
          class="relative top-5 left-3 h-[118px] w-[367px] rounded-[18px] border-5 border-[#394DA8] bg-white text-left"
        >
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
