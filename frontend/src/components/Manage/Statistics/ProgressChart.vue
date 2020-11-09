<template>
  <div class="common-font">
		<span class="no-wrap mb-2"><b>{{totalCount}}</b> - Total Count</span>
		<!-- 국가명, 클릭수, 막대 반복표시 -->
		<div 
			v-for="(item, index) in sortedItems" 
			:key="item[0]"
		>
			<div class="d-flex justify-space-between pb-1">
				<!-- 국가명 -->
				<div>{{item[0]}}</div>
				<!-- 클릭수 -->
				<div>
					{{formatNumber(item[1])}}
				</div>
			</div>
			<!-- 막대 -->
			<div 
				:style="{
					'background-color': (index === 0) ? colorHighest : colorNormal,
					'height': '4px',
					'width': calculateWidth(item[1])
				}"
				class="mb-1"
			/>
		</div>

		<div class="grey--text" v-if="isDataEmpty()">No Data.</div>
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
			if (this.isDataEmpty(items))
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
		},
		isDataEmpty() {
			return this.items === null || Object.keys(this.items).length === 0
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
	},
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