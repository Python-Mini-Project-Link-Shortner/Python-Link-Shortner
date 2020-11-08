<!-- 국가별 통계 
* Props
	- colorLow: 낮은 값일 때의 색상
	- colorHigh: 높은 값을 때의 색상
	- data: 적용할 국가별 데이터 (배열)
-->
<template>
	<div class="display-flex flex-row" ref="parent">
		<div ref="pChart">
			<ProgressChart 
				class="my-2 px-2"
				:items="countries"/>
		</div>

		<div class="flex-grow">
			<div :id="_uid" />
		</div>
	</div>
</template>

<script>
import {mapState} from 'vuex'
import ProgressChart from '@/components/Manage/Statistics/ProgressChart.vue'

export default {
	name: 'GeoChart',
	data: () => ({
		dataHeader: ['Country', 'Clicks'],
		breakpoint: null,
		responsiveWidth: '100%',
	}),
	computed: {
		...mapState(['googleMapAPI']),
		countries() {
			return {
				'Germany': 200,
				'United States': 300,
				'Brazil': 400,
				'Canada': 1500
			}
		},
		dataArray() {
			const countries = this.countries
			let res = []
			res.push(this.dataHeader)
			for (const country in countries) {
				res.push([country, countries[country]])
			}

			return google.visualization.arrayToDataTable(res)
		},
		options() {
			return {
				height: '210',
				width: this.responsiveWidth,
				colorAxis: {colors: ['#e1f7fc', '#3773a5']},
				legend: 'none'
			}
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
	methods: {
		drawGeoChart() {
			let chart = new google.visualization.GeoChart(document.getElementById(this._uid))

			chart.draw(this.dataArray, this.options)
		},
		redrawChart() {
			// 화면 사이즈가 변경되면 크기 새로고침
			const currentBreakpoint = this.$vuetify.breakpoint.name

			if (currentBreakpoint !== this.breakpoint) {
				this.responsiveWidth = this.$refs.parent.clientWidth - this.$refs.pChart.clientWidth
				this.drawGeoChart()
				this.breakpoint = currentBreakpoint
			}
		}
	},
	created() {
		// 1. 구글 GeoChart 그리기
		google.charts.load('current', {
			'packages':['geochart'],
			'mapsApiKey': this.googleMapAPI
		})
		google.charts.setOnLoadCallback(this.drawGeoChart)

		// 2. 현재 Breakpoint 기록 및 변화 시 새로고침
		this.breakpoint = this.$vuetify.breakpoint.name
		window.addEventListener('resize', this.redrawChart)
	},
	beforeDestroy() {
		window.removeEventListener('resize', this.redrawChart)
	},
	components: {
		ProgressChart: ProgressChart,
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