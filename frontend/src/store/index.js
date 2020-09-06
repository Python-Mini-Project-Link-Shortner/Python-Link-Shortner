import Vue from 'vue'
import Vuex from 'vuex'
import main from '@/store/modules/main.js'
import manageModule from '@/store/modules/manageModule.js'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

// https://uxgjs.tistory.com/149 참고사이트
export default new Vuex.Store({
  state: {
    userInfo: {
      loggedIn: false,
      idToken: '',
      email: '',
      name: '',
      expiresAt: null,
    },
    serverURL: {
      login: 'http://127.0.0.1:5000/axios/login',
      shorten:'http://127.0.0.1:5000/ajax',
      linkPageURL: 'http://127.0.0.1:5000/api/linkList'
    },
    clientID: '623170114008-hftrjkuefmi8aif5jrlsonnu3tv69q7v.apps.googleusercontent.com'
  },
  mutations: {
    setUserInfo(state, payload) {
      Object.keys(payload).forEach(key => {
        state.userInfo[key] = payload[key]
      })
    },
  },
  actions: {
  },
  modules: {
    main,
    manage: manageModule
  },
  plugins: [createPersistedState()],
})
