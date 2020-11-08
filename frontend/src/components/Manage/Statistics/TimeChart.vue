<template>
  <div :id="_uid" />
</template>

<script>
export default {
	name: 'TimeChart',
	data: () => ({
		dataHeader: ['Day', 'Clicks'],
		breakpoint: null
	}),
	computed: {
		// 지난 14일간의 트래픽 기록
		traffic() {
			const now = new Date()
			let res = []

			for (let i = 1; i < 15; i++) {
				now.setDate(now.getDate() - 1)
				res.push([new Date(now), 1 + Math.random()])
			}

			return res
		},
		// 트래픽 기록을 그래프용 배열로 변환한다.
		dataArray() {
			const traffic = this.traffic
			var formatter = new google.visualization.DateFormat({
				pattern: 'MMM d (EEE)'
			})
			let res = []

			res.push(this.dataHeader)
			traffic.forEach((value) => {
				res.push(value)
			})
			res = google.visualization.arrayToDataTable(res)
			formatter.format(res, 0)

			return res
		},
		options() {
			const traffic = this.traffic
			let hTicks = []
			
			traffic.forEach((value) => {
				hTicks.push(value[0])
			})

			return {
					hAxis: {
						ticks: hTicks,
						gridlines: {color: 'transparent'},
						format: 'MMM d'
					},
					vAxis: {
						gridlines: {count: 1}
					},
					curveType: 'function',
					legend: 'none'
        }
		}
	},
	methods: {
		drawChart() {
			const chart = new google.visualization.LineChart(document.getElementById(this._uid))
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
		// 구글 LineChart 그리기
		google.charts.load('current', {
			'packages':['corechart'],
		})
		google.charts.setOnLoadCallback(this.drawChart)

		// 반응형으로 만들기
		this.breakpoint = this.$vuetify.breakpoint.name
		window.addEventListener('resize', this.redrawChart)
	}
}
</script>

<style scoped>

</style>