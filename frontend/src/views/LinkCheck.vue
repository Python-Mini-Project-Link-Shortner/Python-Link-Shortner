<!-- 원본 링크를 출력하는 컴포넌트 -->
<template>
  <v-card flat class="py-12 mx-auto">
    <!-- <v-list-item two-line>
      <v-list-item-content>
        <v-list-item-title>{{cardText.title}}</v-list-item-title>
        <v-list-item-subtitle>{{cardText.subtitle}}</v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item> -->

    <v-card-title class="">{{cardText.title}}</v-card-title>
    <v-card-subtitle>{{cardText.subtitle}}</v-card-subtitle>
    <v-card-text>
      <div v-for="(line, index) in cardText.content.split('\n')" :key="index">
        {{line}}
      </div>
    </v-card-text>
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
    shortURL: '',     // 7자리 축약 URL
    rawURL: '',       // 원본링크
    msg: '',          // 원본링크 검색 이후 결과 메시지
  }),
  computed: {
    ...mapState(['serverURL']),
    cardText() {
      let title, subtitle, content

      if (this.flag) {
        title = "Hi, Here's the original link."
        subtitle = 'MiniPy URL Checker'
        content = ``
      } else {
        title = 'We are sorry...404.'
        subtitle = "MiniPy URL Checker"
        content = `(${this.shortURL}) \n` +
        `It looks like the link code you provided is broken or not registered. It could also be expired. \n` +
        `Have a nice day!`
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