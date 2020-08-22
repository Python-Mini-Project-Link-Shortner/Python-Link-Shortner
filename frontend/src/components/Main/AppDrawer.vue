<template>
  <v-navigation-drawer
  v-model="drawer"
  app
  light
  temporary
  >

  <v-list rounded>
    <v-list-item-group v-model="tabIndex" color="primary">
      <v-list-item
      v-for="(link, index) in mainLinks"
      :key="link.name"
      :value="index"
      @click="onItemClick(link)"
      >
        <v-list-item-content>
          <v-list-item-title v-text="link.name" />
        </v-list-item-content>
      </v-list-item>
    </v-list-item-group>
  </v-list>
  </v-navigation-drawer>
</template>

<script>
import {mapState, mapMutations} from 'vuex'
import mixRoute from '@/components/mixins/mixRoute.js' // goTo(item)

const main = 'main' // Vuex의 main 모듈

export default {
  name: 'AppDrawer',
  computed: {
    ...mapState(main, ['mainLinks']),
    drawer: {
      get()    { return this.$store.state.main.drawer },
      set(val) { this.setDrawer(val) }
    },
    tabIndex: {
      get()    { return this.$store.state.main.tabIndex },
      set(val) { this.setTabIndex(val) }
    }
  },
  methods: {
    ...mapMutations(main, ['setDrawer', 'setTabIndex', 'setIntersection']),
    onItemClick(item) {
      this.setDrawer(false)
      this.goTo(item)
    }
  },
  mixins: [ mixRoute ]
}
</script>