<template>
  <!-- 스크롤에 반응하는 Jumbotron -->
  <v-parallax class="mb-5" dark :src="imgPath" height="700">
    <v-container class="pb-0" style="max-width: 800px;">
      <!-- 링크 입력하는 텍스트 박스 -->
      <ShortenLink alert />
    </v-container>
  </v-parallax>
</template>

<script>
import ShortenLink from './ShortenLink.vue'

export default {
  name: 'Jumbotron',
  data: () => ({
    imgPath: require('@/assets/img/jumbo 2.jpg')
  }),
  components: {
    ShortenLink
  }
}
</script>

<style scoped>
</style>