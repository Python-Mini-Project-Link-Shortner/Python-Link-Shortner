<template>
  <!-- 스크롤에 반응하는 Jumbotron -->
  <v-parallax class="pb-5" dark :src="imgPath" :height="imgHeight">
    <v-container class="pb-0" style="max-width: 800px;">
      <v-row
      align="center" justify="center"
      :style="{height: imgHeight * 1/3 + 'px'}">
        <v-btn-toggle
          v-model="btnToggle" rounded
          borderless dense mandatory
          color="primary"
        >
          <v-btn :value="'Shorten'" width="100">Shorten</v-btn>
          <v-btn :value="'Check'" width="100">Check</v-btn>
        </v-btn-toggle>
      </v-row>

      <v-row
      align="center" 
      :style="{height: imgHeight * 1/3 + 'px'}">
        <!-- 링크 입력하는 텍스트 박스 -->
        <ShortenLink alert :behavior="btnToggle" :key="btnToggle"/>
      </v-row>

      <v-row
      align="center" 
      :style="{height: imgHeight * 1/3 + 'px'}">
      </v-row>
    </v-container>
  </v-parallax>
</template>

<script>
import ShortenLink from '@/components/ShortenLink.vue'


export default {
  name: 'Jumbotron',
  data: () => ({
    imgPath: require('@/assets/img/jumbo 2.jpg'),
    imgHeight: 700,
    tabItems: [
      {tab: 'Create', component: 'ShortenLink'},
      {tab: 'Check', component: 'CheckLink'}
    ],
    btnToggle: 'Shorten',
  }),
  components: {
    ShortenLink
  }
}
</script>

<style scoped>
</style>