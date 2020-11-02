<!-- 국가별 통계 
* Props
	- colorLow: 낮은 값일 때의 색상
	- colorHigh: 높은 값을 때의 색상
	- data: 적용할 국가별 데이터 (배열)
-->
<template>
	<div class="display-flex flex-row">
		<ProgressChart :items="countries" />

		<div class="flex-grow" :id="_uid">
			
		</div>
	</div>
</template>

<script>
import {mapState} from 'vuex'
import StatProgressChart from '@/components/Manage/StatProgressChart.vue'

export default {
	name: 'GeoChart',
	data: () => ({
		dataHeader: ['Country', 'Clicks'],
	}),
	computed: {
		...mapState(['googleMapAPI']),
		countries() {
			return {
				'Germany': 200,
				'United States': 300,
				'Brazil': 400,
				'Canada': 500
			}
		},
		dataArray() {
			const countries = this.countries
			let res = []
			res.push(this.dataHeader)
			for (const country in countries) {
				res.push([country, countries[country]])
			}

			return res
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
			var data = google.visualization.arrayToDataTable(this.dataArray)
			var options = {
				height: '210',
				colorAxis: {colors: ['#e1f7fc', '#3773a5']},
				legend: 'none'
			}
			var chart = new google.visualization.GeoChart(document.getElementById(this._uid))

			chart.draw(data, options)
		}

		google.charts.setOnLoadCallback(drawRegionsMap)
	},
	components: {
		ProgressChart: StatProgressChart,
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
</style>