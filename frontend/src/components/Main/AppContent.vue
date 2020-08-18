<template>
  <v-main>
    <Jumbotron v-intersect="{
        handler: onIntersect,
        options: {
          threshold: [1.0]
        }
      }" index="0" />

    <Features v-intersect="{
        handler: onIntersect,
        options: {
          threshold: [1.0]
        }
      }" index="1" />
  </v-main>
</template>

<script>
import Jumbotron from './Content/Jumbotron.vue'
import Features from './Content/Features.vue'
import { mapMutations } from 'vuex'

const main = 'main' // Vuex의 'main' 모듈

export default {
  name: 'AppContent',
  methods: {
    ...mapMutations(main, ['setTabIndex']), // Tab 선택을 변경
    onIntersect(entries, observer) {
      const entry = entries[0]

      if (entry.intersectionRatio === 1.0) {
        this.setTabIndex(entry.target.getAttribute('index'))
      }
    }
  },
  components: {
    Jumbotron, Features
  }
}
</script>

<style>

</style>