import Vue from 'vue'
import Vuex from 'vuex'
import main from '@/store/modules/main.js'
import manageModule from '@/store/modules/manageModule.js'

Vue.use(Vuex)

// https://uxgjs.tistory.com/149 참고사이트
export default new Vuex.Store({
  state: {
    userInfo: {
      loggedIn: false,
      idToken: '',
      name: ''
    },
    serverURL: 'http://127.0.0.1:5000/ajax'
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
  }
})
