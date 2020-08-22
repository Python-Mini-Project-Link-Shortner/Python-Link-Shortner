import Vue from 'vue'
import Vuex from 'vuex'
import main from './modules/main.js'
import manageModule from '@/store/modules/manageModule.js'

Vue.use(Vuex)

// https://uxgjs.tistory.com/149 참고사이트
export default new Vuex.Store({
  state: {
    isLogin: false,
    serverURL: 'http://127.0.0.1:5000/ajax'
  },
  mutations: {
    loginSuccess(state) {
      state.isLogin = true
    },
    loginFail(state) {
      state.isLogin = false
    }
  },
  actions: {
  },
  modules: {
    main,
    manage: manageModule
  }
})
