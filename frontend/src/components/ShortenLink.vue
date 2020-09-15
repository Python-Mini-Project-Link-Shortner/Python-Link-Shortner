<template>
  <v-row align="center" justify="center" no-gutters>
    <!-- 링크를 입력하는 텍스트박스 -->
    <v-col class="text-center" cols="12">
      <v-text-field
      v-model="url"
      solo
      clearable
      rounded
      autofocus
      hide-details
      :placeholder="behaviorSetting.placeholderText"
      >
        // 링크 아이콘
        <template slot="prepend-inner">
          <v-icon class="mr-3" size="20" color="rgb(55,115,165)">{{behaviorSetting.icon}}</v-icon>
        </template>

        // Shorten 버튼
        <template slot="append">
          <v-btn color="primary" @click="behaviorHandler">{{behaviorSetting.btnText}}</v-btn>
        </template>
      </v-text-field>
    </v-col>

    <!-- 링크 축약 후 성공/실패 메시지 표시 -->
    <v-col class="mt-3" cols="12" md="10" v-if="alert">
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

          <!-- 메시지 복사 버튼. -->
          <v-col class="py-0 pr-5 text-right"
            v-clipboard="() => alertSetting.msg"
            v-clipboard:success="clipboardSuccess"
            v-clipboard:error="clipboardError"
            v-if="alertSetting.copyBtn">
            <v-btn small outlined>Copy</v-btn>
          </v-col>
        </v-row>
      </v-alert>
    </v-col>

    <!-- 링크 복사에 대한 Snackbar -->
    <div class="text-center" v-if="alert">
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

  </v-row>
</template>

<script>
import {mapState} from 'vuex'
import axios from 'axios'
import {getShortCode} from '@/assets/js/handleURL.js'

export default {
  name: 'ShortenLink',
  data: () => ({
    url: '',
    alertSetting: {
      isSuccess: false,
      copyBtn: true,
      type: 'success',
      msg: 'default'
    },
    snackSetting: {
      show: false,
      color: '',
      msg: ''
    },
    behaviorSetting: {
      btnText: '',
      placeholderText: '',
      icon: ''
    }
  }),
  computed: {
    ...mapState(['serverURL']),
    normalizedBehavior() {
      // null값 방지
      const behavior = (!this.behavior) ? 'Shorten' : this.behavior

      return behavior.trim().toLowerCase()
    }
  },
  props: {
    alert: {
      type: Boolean,
      default: () => false
    },
    behavior: {
      type: String,
      default: () => 'Shorten'
    },
    toggle: {
      type: Boolean,
      default: () => false
    }
  },
  methods: {
    // 동작에 따라 여러 텍스트 및 타입을 설정한다.
    setOnMounted() {
      const behavior = this.normalizedBehavior

      if (behavior === 'shorten') {
        this.behaviorSetting.btnText = 'SHORTEN'
        this.behaviorSetting.placeholderText = 'Input Your Link Here'
        this.behaviorSetting.icon = 'fa-link'
      } else if (behavior === 'check') {
        this.behaviorSetting.btnText = 'CHECK'
        this.behaviorSetting.placeholderText = 'Input Your Shortend Link Here'
        this.behaviorSetting.icon = 'done_outline'
      }
    },
    // 동작을 결정할 메소드
    behaviorHandler() {
      const behavior = this.normalizedBehavior
      if (behavior === 'shorten') {
        this.shortenURL()
      } else if (behavior === 'check') {
        this.checkURL()
      }
    },
    // 서버로부터 축약 링크를 반환받는다. => Shorten 버튼
    shortenURL() {
      axios.post(this.serverURL['shorten'], {url: this.url})
        .then( res => {
          const alert = this.alertSetting

          alert.isSuccess = true                                // 반환 후 아래에 메시지를 표시한다.
          alert.type = res.data.flag ? 'success' : 'warning'    // 메시지 박스의 테마
          alert.msg = res.data.msg                              // 표시할 메시지
        }).catch( ex => {
          console.log(ex)
        })
    },
    checkURL() {
      const result = getShortCode(this.url)

      // 올바른 URL 형식인지 검사한다.
      if (!result.flag) {
        alert(result.msg)
        return
      }

      // LinkCheck 페이지로 이동한다.
      this.$router.push({
        name: 'LinkCheck',
        params: {shortURL: result.shortCode}
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
  },
  mounted() {
    this.setOnMounted()
  }
}
</script>