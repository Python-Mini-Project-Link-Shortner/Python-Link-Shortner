<template>
  <v-btn color="rgb(55,115,165)" dark outlined :block="block" :id="_uid">
    <v-row justify="space-around" align="center">
      <v-col cols="auto" class="px-0">
        <v-avatar tile size="26">
          <img src="@/assets/img/Google Logo.png" alt="">
        </v-avatar>
      </v-col>
      <v-col cols="auto" class="pa-1" :class="{'text-small': long}">
        {{loginText}}
      </v-col>
    </v-row>
  </v-btn>
</template>

<script>
import {mapState, mapMutations} from 'vuex'
import {userLogin} from '@/assets/js/account.js'
import axios from 'axios'

export default {
  name: 'GLoginBtn',
  computed: {
    ...mapState(['userInfo']),
    loginText() {
      if (this.long) return 'Sign in with Google'
      else return 'Login'
    }
  },
  props: {
    long: {
      type: Boolean,
      default: () => false
    },
    block: {
      type: Boolean,
      default: () => false
    }
  },
  methods: {
    ...mapMutations(['setUserInfo'])
  },
  mounted() {
    const uid = this._uid
    gapi.load('auth2', function() {
      userLogin(uid)
    })
    // gapi.load('auth2', function(){
    //   // 로그인 기능을 적용할 요소
    //   const element = document.getElementById(this._uid)
    //   // OAuth2 기능을 활성화한다.
    //   const auth2 = gapi.auth2.init({
    //     client_id: '623170114008-hftrjkuefmi8aif5jrlsonnu3tv69q7v.apps.googleusercontent.com',
    //   })

    //   // 로그인 기능을 적용한다. 1: 적용할 요소, 2: 옵션, 3: 성공시 콜백함수
    //   auth2.attachClickHandler(element, {}, function(googleUser) {
    //       const authResponse = googleUser.getAuthResponse()
    //       const loggedIn = true
    //       const idToken = authResponse.id_token
    //       const name = googleUser.getBasicProfile().getName()

    //       // 유저 정보를 Vuex에 담고, Manage 페이지로 포워딩
    //       this.setUserInfo({loggedIn, idToken, name})
    //       this.$router.push({name: 'Manage'})
    //   }.bind(this))
    // }.bind(this)) 
  }
}
</script>

<style scoped>
.text-small {
  text-transform: none !important;
  font-size: 1em;
  margin-left: 6px;
}
</style>