<template>
  <v-container class="mx-auto px-8">
		<v-row>
			<v-col>
				<StatSubHeader 
					title="countries"
					subtitle="Overall Period"
				/>
				<GeoChart />
			</v-col>
		</v-row>
  </v-container>
</template>

<script>
import GeoChart from '@/components/Manage/GeoChart.vue'
import StatSubHeader from '@/components/Manage/StatSubHeader.vue'
export default {
	name: 'Statistics',
	props: {

	},
	components: {
		GeoChart, StatSubHeader
	}
}
</script>

<style>

</style>