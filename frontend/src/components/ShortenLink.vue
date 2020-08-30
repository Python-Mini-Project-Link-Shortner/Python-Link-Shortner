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
      placeholder="Input Your Link Here."
      >
        <template slot="append">
          <v-btn color="primary" @click="shortenURL">Shorten</v-btn>
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
          <v-col class="py-0 pr-5 text-right"
            v-clipboard="() => alertSetting.msg"
            v-clipboard:success="clipboardSuccess"
            v-clipboard:error="clipboardError">
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

export default {
  name: 'ShortenLink',
  data: () => ({
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
  props: {
    alert: {
      type: Boolean,
      default: () => false
    }
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
  },
  computed: {
    ...mapState(['serverURL'])
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Recursive:wght@300;400;500&display=swap');
.logo {
	font-family: 'Recursive', sans-serif;
	font-weight: 300;
	font-size: 2em;
	text-decoration: none;
	color: inherit;
}
.logo .py {
	color: rgb(55,115,165);
}
.no-drag {
	-ms-user-select: none; 
	-moz-user-select: -moz-none;
	-webkit-user-select: none; 
	-khtml-user-select: none; 
	user-select:none;
}
</style>