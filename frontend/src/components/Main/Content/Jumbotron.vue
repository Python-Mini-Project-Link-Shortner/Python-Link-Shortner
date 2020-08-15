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
                        <v-btn color="primary" @click="shortenURL">Shorten</v-btn>
                    </template>
                </v-text-field>
            </v-col>

            <v-col cols="12" md="10">
                <v-alert 
                  :value="alertSetting.isSuccess"
                  :type="alertSetting.type" 
                  class="ma-0" 
                  dense 
                  dark 
                  dismissible
                  >
                    <v-row justify="space-around" align="center">
                        <v-col class="py-0 pl-5">
                            {{alertSetting.msg}}
                        </v-col>
                        <v-col class="py-0 pr-5 text-right">
                            <v-btn small outlined>Copy</v-btn>
                        </v-col>
                    </v-row>
                </v-alert>
            </v-col>
        </v-row>  
    </v-container>
</v-parallax>
</template>

<script>
import axios from 'axios'
import {mapState} from 'vuex'

export default {
    name: 'Jumbotron',
    data: () => ({
        imgPath: require('@/assets/img/jumbo 2.jpg'),
        url: '',
        alertSetting: {
            isSuccess: false,
            type: 'success',
            msg: 'default'
        }
    }),
    computed: {
        ...mapState(['serverURL'])
    },
    methods: {
        shortenURL() {
            axios.post(this.serverURL, {url: this.url})
              .then( res => {
                  const alert = this.alertSetting
                  alert.isSuccess = res.data.flag
                  alert.type = res.data.flag ? 'success' : 'warning'
                  alert.msg = res.data.msg
                  console.log(res.data)
              }).catch( ex => {
                  console.log(ex)
              })

        }
    }
}
</script>

<style scoped>
</style>