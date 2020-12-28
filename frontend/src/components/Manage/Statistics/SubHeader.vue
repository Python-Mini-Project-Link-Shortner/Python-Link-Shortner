<template>
  <div class="d-flex">
		<!-- 아이콘 영역 -->
		<div class="mr-2">
			<v-icon size="20" color="indigo">
				fa-arrow-alt-circle-right
			</v-icon>
		</div>

		<!-- 제목, 소제목 영역 -->
		<div>
			<div class="text-title">
				{{title}}
			</div>
			<div class="text-subtitle">
				{{subtitle}}
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'StatSubHeader',
	props: {
		title: {
			type: String,
			default: () => ''
		},
		subtitle: {
			type: String,
			default: () => ''
		}
	}
}
</script>

<style scoped>
.text-title {
	font-family: 'Times New Roman', Times, serif;
	line-height: 1rem;
	letter-spacing: 1.5px;
	text-transform: uppercase;
	padding-top: 5px;
}
.text-subtitle {
	font-size: 0.75rem;
	color: grey;
}

</style>