<!-- 국가별 통계 
* Props
	- colorLow: 낮은 값일 때의 색상
	- colorHigh: 높은 값을 때의 색상
	- data: 적용할 국가별 데이터 (배열)
-->
<template>
	<div>
		<div :id="_uid">
				
		</div>
	</div>
</template>

<script>
import {mapState} from 'vuex'

export default {
	name: 'GeoChart',
	computed: {
		...mapState(['googleMapAPI']),
		dataArray() {
			let data = [['Country', 'Clicks']]

		}
	},
	props: {
		data: {
			type: Array,
			default: () => [['Country', 'Clicks']]
		},
		width: {
			type: String,
			default: () => '100%'
		},
		height: {
			type: String,
			default: () => ''
		}
	},
	created() {
		google.charts.load('current', {
			'packages':['geochart'],
			'mapsApiKey': this.googleMapAPI
		})

		// 로드 후 적용할 콜백함수
		const drawRegionsMap = () => {
			var data = google.visualization.arrayToDataTable([
				['Country', 'Clicks'],
				['Germany', 200],
				['United States', 300],
				['Brazil', 400],
				['Canada', 500],
				['France', 600],
				['RU', 700]
			])
			var options = {
				height: '210',
				colorAxis: {colors: ['#e1f7fc', '#3773a5']}
			}
			var chart = new google.visualization.GeoChart(document.getElementById(this._uid))

			chart.draw(data, options)
		}

		google.charts.setOnLoadCallback(drawRegionsMap)
	}
}
</script>

<style scoped>
</style>