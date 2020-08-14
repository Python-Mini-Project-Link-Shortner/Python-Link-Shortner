<template>
  <v-parallax dark :src="imgPath" height="700">
    <v-container style="max-width: 800px;">
        <v-row align="center" justify="center" no-gutters>
            <v-col class="text-center" cols="12">
                <v-text-field
                v-model="url"
                solo
                clearable
                rounded
                autofocus
                placeholder="Input Your Link Here."
                >
                    <template slot="append">
                        <v-btn color="primary">Shorten</v-btn>
                    </template>
                </v-text-field>
            </v-col>

            <v-col cols="12" md="10">
                <v-alert 
                  class="ma-0" 
                  type="success" 
                  dense 
                  dark 
                  dismissible
                  >
                  성공!
                </v-alert>

                <v-alert 
                  class="ma-0" 
                  type="warning" 
                  dense 
                  dark 
                  dismissible
                  >
                  실패!
                </v-alert>
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
            url: '',
            isSuccess: false
        }
    },
}
</script>

<style scoped>
</style>