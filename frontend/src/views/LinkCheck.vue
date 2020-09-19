<!-- 원본 링크를 출력하는 컴포넌트 -->
<template>
  <v-card flat class="d-inline-block py-12 mx-auto">
    <v-container>
      <v-row justify="center">
        <v-col cols="auto">
          <v-img 
            class="elevation-2"
            height="300"
            width="300" 
            :src="imgPath" />
        </v-col>

        <v-col align="left" :style="{maxWidth: '500px'}">
          <v-row class="fill-height">
            <v-col cols="12">
              <v-card-subtitle class="pb-0">{{cardText.subtitle}}</v-card-subtitle>
              
              <v-card-title class="pt-0 mb-0 pb-0">
                {{cardText.title}}
              </v-card-title>

              <v-card-text>
                <v-divider class="my-0"/>
                <div class="my-6"></div>
                <div v-for="(line, index) in cardText.content.split('\n')" :key="index">
                  {{line}}
                </div>
              </v-card-text>
            </v-col>
            <v-col align-self="end">
              <div class="pl-4">
                <div class="text-body-2">
                  <span> Your Link: </span>
                  {{origin + '/' + shortURL}}
                </div>
                <v-btn class="mt-2" color="primary">Home</v-btn>
              </div>
            </v-col>
          </v-row>
        </v-col>

      </v-row>
    </v-container>
  </v-card>
</template>
<!-- 타이틀 + 페이지 설명 / Div / 원본 + 축약 -->
<script>
import axios from 'axios'
import {mapState} from 'vuex'

export default {
  name: 'LinkCheck',
  data: () => ({
    flag: null,       // 성공, 실패 여부
    origin: document.location.origin,
    shortURL: '',     // 7자리 축약 URL
    rawURL: '',       // 원본링크
    msg: '',          // 원본링크 검색 이후 결과 메시지
    imgPath: require('@/assets/img/LinkCheck_001.png')
  }),
  computed: {
    ...mapState(['serverURL']),
    cardText() {
      let title, subtitle, content

      if (this.flag) {
        title = this.rawURL
        subtitle = 'You are accessing to'
        content = ``
      } else {
        title = 'Page Not Found'
        subtitle = "We are sorry..."
        content =
        `It looks like the link you provided is broken or not registered.\n` +
        `Please check your link again.`
      }
      return {title, subtitle, content}
    }
  },
  // 페이지 진입 시 원본 URL을 받는다.
  async created() {
    this.shortURL = this.$route.params.shortURL

    try {
      const res = await axios.post(this.serverURL['check'], {url: this.shortURL})

      // 검색에 성공한 경우 링크를 받고, 아닌 경우 에러 메시지를 받는다.
      this.flag = res.data.flag
      if (this.flag === true) {
        this.rawURL = res.data.link
      } else {
        this.msg = res.data.msg
      }
    } catch(e) {
      console.log(e)
    }
  }
}
</script>

<style scoped>

</style>>

</style>