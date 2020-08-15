<template>
  <v-main>
      <Jumbotron />

      <MainFeatures />
  </v-main>
</template>

<script>
import Jumbotron from './Content/Jumbotron.vue'
import MainFeatures from './Content/MainFeatures.vue'
export default {
    name: 'AppContent',
    components: {
        Jumbotron, MainFeatures
    }
}
</script>

<style>

</style>