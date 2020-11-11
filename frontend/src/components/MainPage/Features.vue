<template>
  <div class="pb-9 pt-12" id="features">
    <SubHeader title="Features">
      Those features are combined to create one comprehensive platform, MiniPy.
    </SubHeader>

		<v-container class="limit-width px-6 mx-auto">
			<!-- 슬라이드 컨테니너 -->
			<v-sheet
				class="border-decor mt-12 mb-8"
				elevation="2"
			>
				<v-slide-group
					class="pa-3"
					v-model="slideModel"
				>
					<v-slide-item
						v-for="item in slideItems"
						:key="item.title"
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

export default {
	name: 'Features',
	data: () => ({
		slideModel: null,
		slideItems: [
			{'icon': null, 'title': 'a', 'desc': 'a'},
			{'icon': null, 'title': 'b', 'desc': 'b'},
			{'icon': null, 'title': 'c', 'desc': 'c'},
			{'icon': null, 'title': 'd', 'desc': 'd'},
			{'icon': null, 'title': 'e', 'desc': 'e'}
		]
	}),
	components: {
		SubHeader: SubHeader,
		FeatureCard: FeatureCard
	}
}
</script>

<style scoped>
.border-decor {
  border: 2px solid rgb(55,115,165);
}
</style>