<template>
  <v-app>
      <AppNavBar />
    
      <AppDrawer />

      <AppContent />
  </v-app>
</template>

<script>
import AppNavBar from '@/components/Main/AppNavBar.vue'
import AppDrawer from '@/components/Main/AppDrawer.vue'
import AppContent from '@/components/Main/AppContent.vue'
export default {
    name: 'MainPage',
    components: {
        AppNavBar, AppDrawer, AppContent
    }
}
</script>

<style>

</style>