<template>
  <v-navigation-drawer
  v-model="drawer"
  app
  light
  temporary
  >

  <v-list rounded>
    <v-list-item-group v-model="listIndex" color="primary">
      <v-list-item
      v-for="link in mainLinks"
      :key="link.name"
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
import routeMix from '@/components/mixins/route.js'

const main = 'main' // Vuex의 main 모듈

export default {
  name: 'AppDrawer',
  computed: {
    ...mapState(main, ['mainLinks']),
    drawer: {
      get()    { return this.$store.state.main.drawer },
      set(val) { this.setDrawer(val) }
    },
    listIndex: {
      get()    { return this.$store.state.main.listIndex },
      set(val) { this.setListIndex(val) }
    }
  },
  methods: {
    ...mapMutations(main, ['setDrawer', 'setListIndex', 'setIntersection']),
    onItemClick(item) {
      this.setDrawer(false)
      this.goTo(item)
    }
  },
  mixins: [ routeMix ]
}
</script>