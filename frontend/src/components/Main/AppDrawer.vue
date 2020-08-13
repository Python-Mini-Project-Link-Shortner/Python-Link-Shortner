<template>
  <v-navigation-drawer
    v-model="drawer"
    app
    light
    temporary
    >

    <v-list rounded>
        <v-list-item-group color="primary">
            <v-list-item
            v-for="link in mainLinks"
            :key="link.name"
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

export default {
    name: 'AppDrawer',
    computed: {
        ...mapState(['mainLinks']),
        drawer: {
            get()    { return this.$store.state.drawer },
            set(val) { this.setDrawer(val) }
        }
    },
    methods: {
        ...mapMutations(['setDrawer'])
    }
}
</script>