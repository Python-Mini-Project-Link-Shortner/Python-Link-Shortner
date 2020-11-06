<template>
  <v-container
		class="mx-auto px-8 grey lighten-4"
	>
		<v-row justify="space-around">
			<!-- 국가별 통계 -->
			<v-col cols="6" xl="4">
				<!-- Gutter 적용을 위한 Col 중첩 -->
				<v-col class="white border-decor">
					<SubHeader 
						title="countries"
						subtitle="Overall Period"
					/>

					<GeoChart :height="geoChartHeight"/>
				</v-col>
			</v-col>

			<!-- 기간별 통계 -->
			<v-col cols="6" xl="4">
				<!-- Gutter 적용을 위한 Col 중첩 -->
				<v-col class="white border-decor fill-height">
					<SubHeader 
						title="traffic"
						subtitle="Last 14 days"
					/>

					<TimeChart />
				</v-col>
			</v-col>
		</v-row>
  </v-container>
</template>

<script>
import SubHeader from '@/components/Manage/Statistics/SubHeader.vue'
import GeoChart from '@/components/Manage/Statistics/GeoChart.vue'
import TimeChart from '@/components/Manage/Statistics/TimeChart.vue'
export default {
	name: 'Statistics',
	data: () => ({
		subHeaderHeight: 40
	}),
	computed: {
		geoChartHeight() {
			return (this.window) ? '280' : ''
		}
	},
	props: {
		window: {
			type: Boolean,
			default: () => true
		}
	},
	components: {
		SubHeader: SubHeader,
		GeoChart: GeoChart, 
		TimeChart: TimeChart,
	}
}
</script>

<style scoped>
.display-flex {
	display: flex;
	width: 100%;
	height: 100%;
}
.flex-column {
	flex-direction: column;
}
.flex-row {
	flex-direction: row;
}
.flex-grow {
	flex-grow: 1;
}
.inner-flex {
	display: flex;
	align-items: center;
	justify-content: center;
}
.fill-height {
	height: 100%;
}
.border-decor {
	border: 1px solid #CDCDCD !important;
	border-radius: 8px;
}
</style>