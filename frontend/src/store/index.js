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
      login: 'https://minipy-git.herokuapp.com/api/login',
      authCode: 'https://minipy-git.herokuapp.com/api/authCode',
      shorten:'https://minipy-git.herokuapp.com/api/shorten',
      check: 'https://minipy-git.herokuapp.com/api/check',
      contact: 'https://minipy-git.herokuapp.com/api/contact',
      getStats: 'https://minipy-git.herokuapp.com/api/getStats',
      linkPageURL: 'https://minipy-git.herokuapp.com/api/linkList',
      favoritePageURL: 'https://minipy-git.herokuapp.com/api/favoriteList',
      deleteLinkURL: 'https://minipy-git.herokuapp.com/api/deleteLink',
      changeTagURL: 'https://minipy-git.herokuapp.com/api/changeTag',
      deleteTagURL: 'https://minipy-git.herokuapp.com/api/deleteTag',
      checkFavoriteURL: 'https://minipy-git.herokuapp.com/api/checkFavorite',
      uncheckFavoriteURL: 'https://minipy-git.herokuapp.com/api/uncheckFavorite',
      hideNameListURL: 'https://minipy-git.herokuapp.com/api/hideNameList',
      hideURL: 'https://minipy-git.herokuapp.com/api/hideLink',
      tagListURL: 'https://minipy-git.herokuapp.com/api/tagList',
      hideListURL: 'https://minipy-git.herokuapp.com/api/hideList',
      taggedLinkListURL: 'https://minipy-git.herokuapp.com/api/taggedLinkList'
    },
    googleMapAPI: 'AIzaSyD3iDDJCCjgJoToj7MXi9_ObGp5KCTtsPE',
    clientID: '623170114008-hftrjkuefmi8aif5jrlsonnu3tv69q7v.apps.googleusercontent.com',
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
