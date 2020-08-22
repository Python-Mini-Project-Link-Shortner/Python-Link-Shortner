<template>
  <v-app>
    <AppNavBar />

    <AppDrawer />

    <AppMain />

    <AppFooter />
  </v-app>
</template>

<script>
import AppNavBar from '@/components/Main/AppNavBar.vue'
import AppDrawer from '@/components/Main/AppDrawer.vue'
import AppMain from '@/components/Main/AppMain.vue'
import AppFooter from '@/components/Main/AppFooter.vue'
export default {
  name: 'MainPage',
  components: {
    AppNavBar, AppDrawer, AppMain, AppFooter
  }
}
</script>

<style>
.limit-width {
  max-width: 1200px;
}
</style>