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
      login: 'http://127.0.0.1:5000/api/login',
      authCode: 'http://127.0.0.1:5000/api/authCode',
      shorten:'http://127.0.0.1:5000/api/shorten',
      check: 'http://127.0.0.1:5000/api/check',
      contact: 'http://127.0.0.1:5000/api/contact',
      linkPageURL: 'http://127.0.0.1:5000/api/linkList',
      deleteLinkURL: 'http://127.0.0.1:5000/api/deleteLink',
      changeTagURL: 'http://127.0.0.1:5000/api/changeTag',
      deleteTagURL: 'http://127.0.0.1:5000/api/deleteTag',
      checkFavoriteURL: 'http://127.0.0.1:5000/api/checkFavorite',
      uncheckFavoriteURL: 'http://127.0.0.1:5000/api/uncheckFavorite',
      hideNameListURL: 'http://127.0.0.1:5000/api/hideNameList',
      hideURL: 'http://127.0.0.1:5000/api/hideLink'
    },
    googleMapAPI: 'AIzaSyD3iDDJCCjgJoToj7MXi9_ObGp5KCTtsPE',
    moduleNames:{
      main: 'main',
      manage: 'manage'
    },
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
