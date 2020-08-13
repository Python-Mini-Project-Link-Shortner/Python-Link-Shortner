<template>
  <v-parallax dark :src="imgPath" height="700">
    <v-container style="max-width: 800px;">
        <v-row align="center">
            <v-col class="text-center" cols="12">
                <v-text-field
                v-model="url"
                solo
                clearable
                rounded
                placeholder="Input Your Link Here."
                />
            </v-col>
        </v-row>  
    </v-container>
</v-parallax>
</template>

<script>
export default {
    name: 'Jumbotron',
    data() {
        return {
            imgPath: require('@/assets/img/jumbo 2.jpg'),
            url: ''
        }
    },
    mounted() {
        console.log(this.$vuetify.application.top)
    }
}
</script>

<style>

</style>