<template>
  <div :id="_uid"></div>
</template>

<script>
export default {
	name: 'BrowserChart',
	data: () => ({
		dataHeader: ['Browser', 'Clicks'],
		breakpoint: null
	}),
	computed: {
		browsers() {
			return {
				'Chrome': 10,
				'Safari': 5,
				'Firefox': 8,
			}
		},
		dataArray() {
			const browsers = this.browsers
			let res = []

			res.push(this.dataHeader)
			for (const browser in browsers) {
				res.push([browser, browsers[browser]])
			}

			return google.visualization.arrayToDataTable(res)
		},
		options() {
			return {
				pieHole: 0.4,
			}
		}
	},
	methods: {
		drawChart() {
			const chart = new google.visualization.PieChart(document.getElementById(this._uid))
			chart.draw(this.dataArray, this.options)
		},
		redrawChart() {
			// 화면 사이즈가 변경되면 새로고침
			const currentBreakpoint = this.$vuetify.breakpoint.name

			if (currentBreakpoint !== this.breakpoint) {
				this.drawChart()
				this.breakpoint = currentBreakpoint
			}
		}
	},
	created() {
		google.charts.load("current", {packages:["corechart"]});
		google.charts.setOnLoadCallback(this.drawChart);
	},
	beforeDestroy() {

	}
}
</script>

<style>

</style>