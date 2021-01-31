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
      linkListURL: 'https://minipy-git.herokuapp.com/api/linkList',
      favoriteListURL: 'https://minipy-git.herokuapp.com/api/favoriteList',
      checkFavoriteURL: 'https://minipy-git.herokuapp.com/api/checkFavorite',
      uncheckFavoriteURL: 'https://minipy-git.herokuapp.com/api/uncheckFavorite',
      deleteLinkURL: 'https://minipy-git.herokuapp.com/api/deleteLink',
      tagListURL: 'https://minipy-git.herokuapp.com/api/tagList',
      taggedLinkListURL: 'https://minipy-git.herokuapp.com/api/taggedLinkList',
      changeTagURL: 'https://minipy-git.herokuapp.com/api/changeTag',
      deleteTagURL: 'https://minipy-git.herokuapp.com/api/deleteTag',
      hideNameListURL: 'https://minipy-git.herokuapp.com/api/hideNameList',
      hiddenLinkListURL: 'https://minipy-git.herokuapp.com/api/hiddenLinkList',
      hideURL: 'https://minipy-git.herokuapp.com/api/hideLink',
      unhideURL: 'https://minipy-git.herokuapp.com/api/unhideLink'
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
