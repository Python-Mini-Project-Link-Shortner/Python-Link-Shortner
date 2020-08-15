<template>
  <!-- 스크롤에 반응하는 Jumbotron -->
  <v-parallax dark :src="imgPath" height="700">
    <v-container style="max-width: 800px;">
        <v-row align="center" justify="center" no-gutters>
            <!-- 링크 입력하는 텍스트 박스 -->
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

            <!-- 링크 축약 후 결과 메시지 표시 -->
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
                        <v-col class="py-0 pr-5 text-right"
                          v-clipboard="() => snackSetting.msg"
                          v-clipboard:success="clipboardSuccess"
                          v-clipboard:error="clipboardError">
                            <v-btn small outlined>Copy</v-btn>
                        </v-col>
                    </v-row>
                </v-alert>
            </v-col>
        </v-row>  
    </v-container>

    <!-- 링크 복사에 대한 Snackbar -->
    <div class="text-center ma-2">
        <v-snackbar
        v-model="snackSetting.show"
        :color="snackSetting.color"
        top
        timeout="3000"
        >
        {{ snackSetting.msg }}

        <template v-slot:action="{ attrs }">
            <v-btn
            text
            v-bind="attrs"
            @click="snackSetting.show = false"
            >
            Close
            </v-btn>
        </template>
        </v-snackbar>
    </div>


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
        },
        snackSetting: {
            show: false,
            color: '',
            msg: ''
        }
    }),
    computed: {
        ...mapState(['serverURL'])
    },
    methods: {
        // 서버로부터 축약 링크를 반환받는다. => Shorten 버튼
        shortenURL() {
            axios.post(this.serverURL, {url: this.url})
              .then( res => {
                  const alert = this.alertSetting

                  alert.isSuccess = res.data.flag                       // 반환 후 아래에 메시지를 표시한다.
                  alert.type = res.data.flag ? 'success' : 'warning'    // 메시지 박스의 테마
                  alert.msg = res.data.msg                              // 표시할 메시지
              }).catch( ex => {
                  console.log(ex)
              })
        },
        clipboardSuccess() {
            const snack = this.snackSetting

            snack.show = true
            snack.msg = 'Copied Successfully'
            snack.color = 'success'
        },
        clipboardError() {
            const snack = this.snackSetting

            snack.show = true
            snack.msg = 'Copy failed'
            snack.color = 'warning'
        }
    }
}
</script>

<style scoped>
</style>