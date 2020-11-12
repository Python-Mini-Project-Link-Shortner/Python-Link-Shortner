<template>
  <div class="pb-9" id="features">
	<HSpacer class="mb-9" />

  <SubHeader title="Features">
    Those features are combined to create one comprehensive platform, MiniPy.
  </SubHeader>

    <v-container class="limit-width px-6 mx-auto">
      <!-- 슬라이드 컨테니너 -->
      <v-sheet
        class="border-decor mt-12 mb-8"
        elevation="2"
        @mouseenter="haltSlide"
        @mouseleave="resumeSlide"
      >
        <v-slide-group
          class="pa-3"
          v-model="slideModel"
					show-arrows="always"
        >
          <v-slide-item
            v-for="(item, idx) in slideItems"
            :key="idx"
						center-active
          >
            <FeatureCard
              class="ma-8 mx-10"
              :title="item.title"
              :desc="item.desc"
            />
          </v-slide-item>
        </v-slide-group>
      </v-sheet>
    </v-container>
  </div>
</template>

<script>
import SubHeader from '@/components/MainPage/SubHeader.vue'
import FeatureCard from '@/components/MainPage/FeatureCard.vue'
import HSpacer from '@/components/MainPage/HSpacer.vue'

export default {
  name: 'Features',
  data: () => ({
    slideModel: null,
    slideItems: [
      {'icon': null, 'title': 'a', 'desc': 'a', 'idx': 0},
      {'icon': null, 'title': 'b', 'desc': 'b', 'idx': 1},
      {'icon': null, 'title': 'c', 'desc': 'c', 'idx': 2},
      {'icon': null, 'title': 'd', 'desc': 'd', 'idx': 3},
      {'icon': null, 'title': 'e', 'desc': 'e', 'idx': 4}
    ],
    pauseSlide: false,
  }),
  components: {
    SubHeader: SubHeader,
		FeatureCard: FeatureCard,
		HSpacer: HSpacer
	},
	methods: {
    activateCard(idx) {
      console.log('hi')
      this.slideModel = idx
    },
    haltSlide() {
      this.pauseSlide = true
    },
    resumeSlide() {
      this.pauseSlide = false
    },
    consoleLog() {
      console.log('HI')
    }
  },
  created() {
    setInterval(() => {
      if (this.pauseSlide) return

      const curSlide = this.slideModel
      const maxIndex = this.slideItems.length - 1

      this.slideModel = (curSlide == maxIndex) ? 0 : curSlide + 1
    }, 8000)
  },
	watch: {
		slideModel: {
			handler: function() {
				console.log(this.slideModel)
			}
		}
	}
}
</script>

<style scoped>
.border-decor {
  border: 2px solid rgb(55,115,165);
}
</style>