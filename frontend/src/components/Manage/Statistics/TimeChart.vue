<template>
  <div :id="_uid" />
</template>

<script>
import {mapState} from 'vuex'
import {isSameDate, DateDiff} from '@/assets/js/time.js'

export default {
	name: 'TimeChart',
	data: () => ({
		dataHeader: ['Day', 'Clicks'],
		dataProvided: false,
		breakpoint: null
	}),
	computed: {
		...mapState('manage', ['statData']),
		// 지난 14일간의 트래픽 기록
		traffic() {
			const now = new Date()

			// 기본값 초기화
			this.dataProvided = false

			// 반환 형식 설정
			let res = []
			for (let i = 0; i < 14; i++) {
				res.push([new Date(now), 0])
				now.setDate(now.getDate() - 1)
			}
			
			// 유효성 검사
			let timeData = this.statData.time
			if (typeof timeData !== "undefined")
				timeData = timeData.map(timeStr => new Date(Date.parse(timeStr)))
			else 
				return res

			// 14일 차이 이하라면 배열에 저장
			let cntArray = new Array(14).fill(0)
			timeData.forEach(time => {
				let dayDiff = DateDiff.inDays(time, now)
				
				if (dayDiff < 14) cntArray[dayDiff] += 1
			})
			this.dataProvided = (cntArray.some(cnt => cnt > 0)) ? true : false

			for (let i = 0; i < 14; i++) {
				now.setDate(now.getDate() - 1)
				res.push([new Date(now), cntArray[i]])
			}

			return res
		},
		// 트래픽 기록을 그래프용 배열로 변환한다.
		dataArray() {
			const traffic = this.traffic
			const formatter = new google.visualization.DateFormat({
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
			
			// 가로축 값: 최근 14일
			traffic.forEach((value) => {
				hTicks.push(value[0])
			})

			// 가로축 최소값
			let viewWindowMin = (this.dataProvided) ? -0.2 : 0

			return {
					hAxis: {
						ticks: hTicks,
						gridlines: {color: 'transparent'},
						format: 'MMM d'
					},
					vAxis: {
						viewWindow: {
							min: viewWindowMin
						},
						gridlines: {count: 1}
					},
					curveType: 'function',
					legend: 'none'
        }
		}
	},
	watch: {
		statData: {
			handler: function() {
				this.drawChart()
			}
		}
	},
	methods: {
		drawChart() {
			const chart = new google.visualization.LineChart(document.getElementById(this._uid))
			chart.draw(this.dataArray, this.options)
		},
		makeResponsive() {
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
		window.addEventListener('resize', this.makeResponsive)
	},
	beforeDestroy() {
		window.removeEventListener('resize', this.makeResponsive)
	},
}
</script>

<style scoped>

</style>