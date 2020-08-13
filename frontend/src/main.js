import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Clipboard from 'v-clipboard'
import vuetify from './plugins/vuetify';

Vue.use(Clipboard)
Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
