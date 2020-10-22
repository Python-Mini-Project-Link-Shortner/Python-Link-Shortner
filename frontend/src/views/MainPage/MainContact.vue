<template>
	<v-container class="limit-width py-12 mt-8">
		<v-card class="mx-auto" max-width="800">
			<v-row justify="center">
				<!-- 좌측 인사말 카드 -->
				<v-col class="blue-grey lighten-2 py-8" cols="4">
					<v-icon 
					  size="100"
						color="primary">
						fa-envelope-open-text
					</v-icon>
					<div class="text-body-1 white--text font-weight-light my-5 px-3">
						If you have questions or issues with using our service, 
						use the form left. We would be happy to answer your questions 
						and watch your problems solved!
					</div>
				</v-col>

				<!-- 우측 폼 영역 -->
				<v-col cols="8">
					<div class="mt-5 display-1 font-weight-medium grey--text text--darken-2">
						E-mail Us
					</div>
				</v-col>
			</v-row>
		</v-card>
	</v-container>
</template>

<script>
export default {

}
</script>

<style>

</style>