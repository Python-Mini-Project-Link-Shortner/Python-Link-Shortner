<template>
  <v-card 
		class=""
		:color="color"
		min-height="250px" 
		min-width="250px"
	>
		aa
  </v-card>
</template>

<script>
export default {
	name: 'FeatureCard',
	props: {
		icon: {
			type: String,
			default: () => null
		},
		title: {
			type: String,
			default: () => ""
		},
		desc: {
			type: String,
			default: () => ""
		},
		color: {
			type: String,
			default: () => ""
		}
	}
}
</script>

<style scoped>
.border-decor {
	border: black 1px solid !important;
}
</style>