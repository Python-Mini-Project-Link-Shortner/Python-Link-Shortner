<template>
  <v-main>
    <Jumbotron v-intersect="{
        handler: onIntersect,
        options: {
          threshold: [0.0, 1.0]
        }
      }" index="0" />

    <Features v-intersect="{
        handler: onIntersect,
        options: {
          threshold: [0.0, 1.0]
        }
      }" index="1" />
  </v-main>
</template>

<script>
import Jumbotron from './Content/Jumbotron.vue'
import Features from './Content/Features.vue'
import { mapState, mapMutations } from 'vuex'

const main = 'main' // Vuex의 'main' 모듈

export default {
  name: 'AppContent',
  data: () => ({
    intersectInfo: [
      { index: 0, y: 0 },
      { index: 1, y: 0 },
    ]
  }),
  computed: {
    ...mapState(main, ['intersectEnabled', 'tabIndex'])
  },
  methods: {
    ...mapMutations(main, ['setTabIndex']), // Tab 선택을 변경
    onIntersect(entries, observer) {
      const entry = entries[0]
      const targetIndex = Number(entry.target.getAttribute('index'))  // 대상요소 인덱스
      const prevY = this.intersectInfo[targetIndex].y                 // 이벤트 이전의 y 좌표
      const currentY = entry.boundingClientRect.y                     // 현재 y 좌표

      // 클릭에 의한 경우엔 실행하지 않는다.
      if (!this.intersectEnabled) {
        return
      }

      // 화면에 들어온 경우
      if (entry.isIntersecting) {
        if (entry.intersectionRatio === 1.0) {
          this.setTabIndex(targetIndex)
        }
      // 화면에서 벗어날 때까지 메뉴가 바뀌지 않았다면
      } else if (targetIndex === this.tabIndex) {
        // 스크롤을 내린 경우 다음 메뉴로 바꾼다.
        if (prevY > currentY) {
          this.setTabIndex(targetIndex + 1)
        // 스크롤을 올린 경우 이전 메뉴로 바꾼다.
        } else if (prevY < currentY) {
          this.setTabIndex(targetIndex - 1)
        }
      }

      // 대상 요소의 y 좌표를 저장한다.
      this.intersectInfo[targetIndex].y = currentY
    }
  },
  components: {
    Jumbotron, Features
  }
}
</script>

<style>

</style>