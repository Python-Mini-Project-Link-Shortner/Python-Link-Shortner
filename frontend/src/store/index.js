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
      linkPageURL: 'http://127.0.0.1:5000/api/linkList',
      favoritePageURL: 'http://127.0.0.1:5000/api/favoriteList',
      deleteLinkURL: 'http://127.0.0.1:5000/api/deleteLink',
      changeTagURL: 'http://127.0.0.1:5000/api/changeTag',
      deleteTagURL: 'http://127.0.0.1:5000/api/deleteTag',
      checkFavoriteURL: 'http://127.0.0.1:5000/api/checkFavorite',
      uncheckFavoriteURL: 'http://127.0.0.1:5000/api/uncheckFavorite',
      hideNameListURL: 'http://127.0.0.1:5000/api/hideNameList',
      hideURL: 'http://127.0.0.1:5000/api/hideLink',
    },
    moduleNames:{
      main: 'main',
      manage: 'manage'
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
