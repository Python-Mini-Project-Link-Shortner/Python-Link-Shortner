<template>
  <v-app>
      <AppNavBar />
    
      <AppDrawer />

      <AppContent />

      <AppFooter />
  </v-app>
</template>

<script>
import AppNavBar from '@/components/Main/AppNavBar.vue'
import AppDrawer from '@/components/Main/AppDrawer.vue'
import AppContent from '@/components/Main/AppContent.vue'
import AppFooter from '@/components/Main/AppFooter.vue'
export default {
    name: 'MainPage',
    components: {
        AppNavBar, AppDrawer, AppContent, AppFooter
    }
}
</script>

<style>

</style>