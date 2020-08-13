import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Clipboard from 'v-clipboard'

Vue.use(Buefy)
Vue.use(Clipboard)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
