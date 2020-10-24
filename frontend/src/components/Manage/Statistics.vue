<template>
  <v-container class="mx-auto px-8">
		<GeoChart />
  </v-container>
</template>

<script>
import GeoChart from '@/components/Manage/GeoChart.vue'
export default {
	name: 'Statistics',
	props: {

	},
	components: {
		GeoChart
	}
}
</script>

<style>

</style>