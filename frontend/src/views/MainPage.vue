<template>
  <v-app>
        <AppNavBar />
    
        <AppDrawer />
  </v-app>
</template>

<script>
import AppNavBar from '@/components/Main/AppNavBar.vue'
import AppDrawer from '@/components/Main/AppDrawer.vue'
export default {
    name: 'MainPage',
    components: {
        AppNavBar, AppDrawer
    }
}
</script>

<style>

</style>