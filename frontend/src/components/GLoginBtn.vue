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
    // 로그인 기능 할당
    const uid = this._uid
    gapi.load('auth2', function() {
      userLogin(uid)
    })
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