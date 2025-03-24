<script setup lang="ts">
import SmartSvg from '@/components/smart/SmartSvg.vue';
import { inject, onMounted, ref, useTemplateRef, watch } from 'vue';

interface Image {
  creationdate: string;
  doodle: string;
  generated: string;
  id: number;
}

const startOverlay = inject('start-overlay', () => {});
const stopOverlay = inject('stop-overlay', () => {});

const refGallery = useTemplateRef('refGallery');

const curPage = ref(0);
const images = ref<Image[]>([]);

async function getImages() {
  try {
    startOverlay();

    const res = await fetch(
      `https://dm.devlos-labs.com/image?limit=5&offset=${curPage.value * 5}`,
      {
        method: 'GET',
      },
    );

    const data = await res.json();

    console.log(data);

    images.value = data.images;

    refGallery.value?.scrollIntoView({
      behavior: 'smooth',
    });
  } finally {
    stopOverlay();
  }
}

watch(curPage, () => {
  getImages();
});

onMounted(() => {
  getImages();
});
</script>

<template>
  <main
    class="font-notebook relative min-h-screen bg-[#E5E6F3] bg-center py-10 text-3xl font-black"
    :style="{ backgroundImage: 'url(/images/background.png)', backgroundRepeat: 'repeat' }"
  >
    <!-- This is for the gallery icon in the top right which links to the gallery page. -->
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
        Gallery
      </div>
    </div>

    <div ref="refGallery">
      <figure v-for="image in images" :key="image.id" class="mx-auto flex w-3/4 gap-1">
        <div class="mb-1 rounded border-4 border-[#394DA8]">
          <img alt="doodle" :src="image.doodle" width="1080" height="720" />
        </div>
        <div class="mb-1 rounded border-4 border-[#394DA8]">
          <img alt="generated" :src="image.generated" width="1080" height="720" />
        </div>
      </figure>
    </div>

    <div class="flex justify-center gap-2 pt-10 pb-15">
      <button
        class="btn border-[#394DA8] bg-[#E5E6F3]"
        :class="{
          'btn-disabled': curPage === 0,
        }"
        type="button"
        @click="--curPage"
      >
        Prev Page
      </button>
      <button class="btn border-[#394DA8] bg-[#E5E6F3]" type="button" @click="++curPage">
        Next Page
      </button>
    </div>
  </main>
</template>
