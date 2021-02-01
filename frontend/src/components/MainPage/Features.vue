<template>
  <div class="pb-9" id="features">
	<HSpacer class="mb-9" />

  <SubHeader title="Features">
    These features are combined to create one comprehensive platform, MiniPy.
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
            <AvatarCard 
              class="ma-8 mx-10 pt-5"
              minHeight="250px" minWidth="250px" maxWidth="250px" 
              iconSize="60" :icon="item.icon"
              borderColor="transparent" hoverWidth="1"
              titleSize="1.2"
              textContent="text-center"
            >
              <template v-slot:title>
                {{item.title}}
              </template>

              <template v-slot:content>
                {{item.desc}}
              </template>
            </AvatarCard>

          </v-slide-item>
        </v-slide-group>
      </v-sheet>
    </v-container>
  </div>
</template>

<script>
import SubHeader from '@/components/MainPage/SubHeader.vue'
import AvatarCard from '@/components/MainPage/AvatarCard.vue'
import HSpacer from '@/components/MainPage/HSpacer.vue'

export default {
  name: 'Features',
  data: () => ({
    slideModel: null,
    slideItems: [
      {
        'icon': 'fa-chart-bar', 
        'title': 'Traffic Tracing', 
        'desc': 'You can collect access and traffic information by looking at the simplified graph in your dashboard.'
      },
      {
        'icon': 'fa-id-badge',
        'title': 'Personal Profile',
        'desc': 'Personal Profile is automatically created via Google Login. No additional personal data is required.'
      },
      {
        'icon': 'fa-check-square', 
        'title': 'Link Check', 
        'desc': 'By attaching # after a link or by using the check tab above, suspicious links can be verified beforehand.'
        },
    ],
    pauseSlide: false,
  }),
  components: {
    SubHeader: SubHeader,
    AvatarCard: AvatarCard,
		HSpacer: HSpacer
	},
	methods: {
    activateCard(idx) {
      console.log('hi')
      this.slideModel = idx
    },
    consoleLog() {
      console.log('HI')
    }
  },
}
</script>

<style scoped>
.border-decor {
  border: 2px solid rgb(55,115,165);
}
</style>