import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    isLogin: false,
    isLoginError: false,
    mainLinks: [
      {name: 'Main', href: ''},
      {name: 'About', href: ''},
      {name: 'Contact', href: ''}
    ],
    drawer: false,
    serverURL: 'http://127.0.0.1:5000/ajax'
  },
  mutations: {
    loginSuccess(state) {
      state.isLogin = true,
      state.isLoginError = false
    },
    loginError(state) {
      state.isLogin = false,
      state.isLoginError = true
    },
    toggleDrawer(state) {
      state.drawer = !state.drawer
    },
    setDrawer(state, payload) {
      state.drawer = payload
    }
  },
  actions: {
  },
  modules: {
  }
})
