<template>
  <v-app-bar color="white" height="80" app>
    <v-container class="limit-width" fluid>
      <v-row align="center">
        <v-app-bar-nav-icon
        class="hidden-md-and-up" @click="toggleDrawer"
        />
        <!-- MiniPy 타이틀 표시하는 부분 -->
        <v-toolbar-title>
          <Logo />
        </v-toolbar-title>

        <v-spacer />

        <div>
          <v-tabs
          class="hidden-sm-and-down" 
          background-color="transparent"
          slider-size="2"
          v-model="tabIndex"
          >
            <v-tab 
            v-for="item in mainLinks" :key="item.name" 
            :ripple="false" @click="scrollTo(item)"
            >
              {{item.name}}
            </v-tab>
          </v-tabs>
        </div>

        <v-btn color="rgb(55,115,165)" dark class="mx-3">Login</v-btn>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script>
import Logo from './Content/Logo.vue'
import {mapState, mapMutations} from 'vuex'

const main = 'main' // Vuex의 main 모듈

export default {
  name: 'AppNavBar',
  computed: {
    ...mapState(main, ['mainLinks']),
    tabIndex: {
      get()     { return this.$store.state.main.tabIndex },
      set(val)  { this.setTabIndex(val) }
    }
  },
  methods: {
    ...mapMutations(main, ['toggleDrawer', 'setTabIndex']),
    scrollTo(item) {
      this.$vuetify.goTo( 
        item.href === "#" ? 0 : item.href, { duration: 1000 }
      )
    }
  },
  components: {
    Logo
  }
}
</script>