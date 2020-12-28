<template>
  <v-overlay :value="loading" :z-index="9999">
    <v-progress-circular indeterminate size="64"></v-progress-circular>
  </v-overlay>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'LoadingOverlay',
  computed: {
    ...mapState('manage', ['loading'])
  }
}
</script>

<style>
</style>