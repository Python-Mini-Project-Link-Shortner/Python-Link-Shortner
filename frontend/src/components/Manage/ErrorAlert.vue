<template>
  <v-alert type="error" v-if="showError">
    {{ errorMsg }}
  </v-alert>
</template>

<script>
import {mapState} from 'vuex'

export default {
  name: 'ErrorAlert',
  computed: {
    ...mapState('manage', ['errorMsg', 'showError'])
  }
}
</script>

<style>
</style>