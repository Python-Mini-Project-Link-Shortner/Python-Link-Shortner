<template>
  <v-container
		class="mx-auto px-8 grey lighten-4"
	>
		<v-row>
			<v-col class="white" cols="6">
				<v-row>
					<v-col class="py-0">
						<StatSubHeader 
							title="countries"
							subtitle="Overall Period"
						/>
					</v-col>
				</v-row>
				<v-row>
					<v-col>
						<GeoChart :height="geoChartHeight"/>
					</v-col>
				</v-row>
			</v-col>

			<v-col class="py-0">
				<v-col cols="12" class="white" :style="{height: '48%'}">
					<v-row>
						<v-col class="py-0">
							<StatSubHeader 
								title="Total Clicks"
								subtitle="Overall Period"
							/>
						</v-col>
					</v-row>

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
import GeoChart from '@/components/Manage/GeoChart.vue'
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
		GeoChart, StatSubHeader
	}
}
</script>

<style>

</style>