<template>
  <div class="my-2 px-2 common-font">
		<span class="no-wrap mb-2"><b>{{totalCount}}</b> - Total Count</span>
		<!--  -->
		<div 
			v-for="(item, index) in sortedItems" 
			:key="item[0]"
		>
			<div class="d-flex justify-space-between pb-1">
				<div>{{item[0]}}</div>
				<div>
					{{formatNumber(item[1])}}
				</div>
			</div>
			<div 
				:style="{
					'background-color': (index === 0) ? colorHighest : colorNormal,
					'height': '4px',
					'width': calculateWidth(item[1])
				}"
				class="mb-1"
			>

			</div>
		</div>
	</div>
</template>

<script>
import {numberWithCommas} from '@/assets/js/number.js'

export default {
	name: 'StatProgressChart',
	computed: {
		totalCount() {
			let count = 0
			for (const item in this.items) {
				count += this.items[item]
			}

			return numberWithCommas(count)
		},
		sortedItems() {
			const items = this.items
			let res = []

			// 데이터가 없으면 null 반환
			if (Object.keys(items).length === 0)
				return null

			// 객체를 배열에 담고 정렬 후 반환
			for (const item in items) {
				res.push([item, items[item]])
			}
			res.sort(function(a, b) {
				return b[1] - a[1]
			})

			return res
		},
		HighestNumber() {
			return this.sortedItems[0][1]
		}
	},
	methods: {
		calculateWidth(num) {
			const highest = this.HighestNumber
			const ratio = (num / highest) * 100

			return Math.round(ratio) + '%'
		},
		formatNumber(num) {
			return numberWithCommas(num)
		}
	},
	props: {
		items: {
			type: Object,
			default: () => {}
		},
		colorHighest: {
			type: String,
			default: () => '#3773a5'
		},
		colorNormal: {
			type: String,
			default: () => '#a1d9e6'
		},
		maxItem: {
			type: Number,
			default: () => 6
		}
	}
}
</script>

<style scoped>
.common-font {
	font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
	color: black;
	font-size: 0.9rem;
}
.no-wrap {
	display: inline-block;
	white-space: nowrap;
}
</style>