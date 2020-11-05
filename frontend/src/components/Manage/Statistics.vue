<template>
  <v-container
		class="mx-auto px-8 grey lighten-4"
	>
		<v-row>
			<!-- 국가별 통계 -->
			<v-col class="white border-decor" cols="6">
				<v-row>
					<v-col class="py-0">
						<SubHeader 
							title="countries"
							subtitle="Overall Period"
						/>
					</v-col>
				</v-row>

				<GeoChart :height="geoChartHeight"/>
			</v-col>

			<!-- 기간별 통계 -->
			<v-col class="py-0">
				<v-col cols="12" class="white" :style="{height: '48%'}">
					<div class="display-flex flex-column flow-column">
						<div>
							<SubHeader 
								title="Total Clicks"
								subtitle="Overall Period"
							/>
						</div>
						<div class="flex-grow inner-flex display-2 primary--text">
							5000
						</div>
					</div>

					<v-row>
						<v-col class="py-0">

						</v-col>
					</v-row>
				</v-col>

				<v-col class="pt-0" :style="{height: '4%'}"></v-col>

				<v-col class="white" :style="{height: '48%'}">
						aa
				</v-col>
			</v-col>
		</v-row>
  </v-container>
</template>

<script>
import StatGeoChart from '@/components/Manage/StatGeoChart.vue'
import StatSubHeader from '@/components/Manage/StatSubHeader.vue'
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
		GeoChart: StatGeoChart, 
		SubHeader: StatSubHeader,
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
.border-decor {
	border: 1px solid #CDCDCD !important;
	border-radius: 8px;
}
</style>