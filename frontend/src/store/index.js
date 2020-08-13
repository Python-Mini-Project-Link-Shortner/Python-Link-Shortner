import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: false,
    isLoginError: false
  },
  mutations: {
    loginSuccess(state) {
      state.isLogin = true,
      state.isLoginError = false
    },
    loginError(state) {
      state.isLogin = false,
      state.isLoginError = true
    }
  },
  actions: {
  },
  modules: {
  }
})
