import Vue from 'vue'
import Vuex from 'vuex'
import main from './modules/main.js'

Vue.use(Vuex)

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
    main
  }
})
