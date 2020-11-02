<template>
  <div>
		<span>{{totalCount}} - Total Count</span>
		<!--  -->
		<div 
			v-for="item in sortedItems" 
			:key="item[0]"
		>
			<div class="d-flex justify-space-between">
				<div>{{item[0]}}</div>
				<div>
					{{item[1]}}
				</div>
			</div>
			<div :style="{
				'background-color': colorHighest,
				'height': '5px',
				'width': '100%'
			}">

			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'StatProgressChart',
	computed: {
		totalCount() {
			let count = 0
			for (const item in this.items) {
				count += this.items[item]
			}

			return count
		},
		sortedItems() {
			const items = this.items
			let res = []

			// 객체를 배열에 담기
			for (const item in items) {
				res.push([item, items[item]])
			}
			// 배열 정렬하기
			res.sort(function(a, b) {
				return b[1] - a[1]
			})

			return res
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
			default: () => '#e1f7fc'
		}
	}
}
</script>

<style>

</style>