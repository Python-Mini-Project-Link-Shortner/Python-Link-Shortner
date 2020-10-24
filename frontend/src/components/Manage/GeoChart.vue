<!-- 국가별 통계 
* Props
	- colorLow: 낮은 값일 때의 색상
	- colorHigh: 높은 값을 때의 색상
	- data: 적용할 국가별 데이터
-->
<template>
  <div id="unique">

	</div>
</template>

<script>
import {mapState} from 'vuex'

export default {
	name: 'GeoChart',
	computed: {
		...mapState(['googleMapAPI'])
	},
	methods: {
		drawRegionsMap() {
			var data = google.visualization.arrayToDataTable([
				['Country', 'Clicks'],
				['Germany', 200],
				['United States', 300],
				['Brazil', 400],
				['Canada', 500],
				['France', 600],
				['RU', 700]
			]);

			var options = {};
			var chart = new google.visualization.GeoChart(document.getElementById('unique'));

			chart.draw(data, options);
		}
	},
	created() {
		google.charts.load('current', {
			'packages':['geochart'],
			'mapsApiKey': this.googleMapAPI
		});
		google.charts.setOnLoadCallback(this.drawRegionsMap);
	}
}
</script>

<style scoped>
</style>