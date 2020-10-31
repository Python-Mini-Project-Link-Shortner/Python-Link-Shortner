<template>
  <!-- 스크롤에 반응하는 Jumbotron -->
  <v-parallax class="pb-5" dark :src="imgPath" :height="imgHeight">
    <v-container class="pb-0" style="max-width: 800px;">
      <v-row
      align="center" justify="center"
      :style="{height: imgHeight * 1/3 + 'px'}">
        <v-btn-toggle
          v-model="btnToggle" rounded
          borderless dense
          color="primary"
          :key="forceUpdate"
        >
          <v-tooltip :value="btnToggle === 'Shorten'" bottom>
            <template v-slot:activator="{ attrs }">
              <v-btn :value="'Shorten'" width="100" v-bind="attrs">
                Shorten
              </v-btn>
            </template>
            <span>Create a short link</span>
          </v-tooltip>

          <v-tooltip :value="btnToggle === 'Check'" bottom>
            <template v-slot:activator="{ attrs }">
              <v-btn :value="'Check'" width="100" v-bind="attrs">
                Check
              </v-btn>
            </template>
            <span>Check the original link</span>
          </v-tooltip>
        </v-btn-toggle>
      </v-row>

      <!-- 링크 입력하는 텍스트 박스 -->
      <v-row
      align="center" 
      :style="{height: imgHeight * 1/3 + 'px'}">
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
    btnToggle: null,
    forceUpdate: 1,
  }),
  methods: {
    // forceUpdate 값을 변경한다.
    tooltipUpdate() {
      const temp = String(this.btnToggle)
      
      // DOM 업데이트 후 툴팁을 다시 표시한다.
      this.btnToggle = ''
      this.$nextTick(() => {
        this.btnToggle = temp
      })

      // 툴팁 컴포넌트를 업데이트한다.
      this.forceUpdate = this.forceUpdate * (-1)
    }
  },
  mounted() {
    // Mounted 시점에서 모든 DOM 요소가 업데이트 된 이후 탭 선택
    this.$nextTick(() => {
      this.btnToggle = 'Shorten'
    })
  },
  created() {
    window.addEventListener('resize', this.tooltipUpdate)
  },
  destroyed() {
    window.removeEventListener('resize', this.tooltipUpdate)
  },
  components: {
    ShortenLink
  },
}
</script>

<style scoped>
.v-tooltip__content {
  z-index: 4 !important;
}
.v-tooltip__content::after {
  content: '';
  border: solid 8px transparent;
  border-bottom-color: rgba(97, 97, 97, 0.9);
  position: absolute;
  bottom: 100%;
  right: 50%;
  margin-right: -8px;
}
</style>