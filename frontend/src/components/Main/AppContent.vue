<template>
  <v-main>
    <Jumbotron />

    <Features />
  </v-main>
</template>

<script>
import Jumbotron from './Content/Jumbotron.vue'
import Features from './Content/Features.vue'
export default {
  name: 'AppContent',
  components: {
    Jumbotron, Features
  }
}
</script>

<style>

</style>