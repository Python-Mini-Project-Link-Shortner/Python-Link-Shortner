import Vue from 'vue'
import Vuex from 'vuex'
import manageModule from '@/store/modules/manageModule.js'

Vue.use(Vuex)

// https://uxgjs.tistory.com/149 참고사이트
export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    manage: manageModule
  }
})
