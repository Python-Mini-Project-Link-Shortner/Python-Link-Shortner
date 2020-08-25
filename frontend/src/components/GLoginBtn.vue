<template>
  <v-btn class="mx-3" color="rgb(55,115,165)" dark outlined>
    <v-row justify="space-between" align="center">
      <v-col class="px-0">
        <v-avatar tile size="26">
          <img src="@/assets/img/Google Logo.png" alt="">
        </v-avatar>
      </v-col>
      <v-col class="pa-1" :class="{'text-small': long}">
        {{loginText}}
      </v-col>
    </v-row>
  </v-btn>
</template>

<script>
export default {
    name: 'GLoginBtn',
    computed: {
      loginText() {
        if (this.long) return 'Sign in with Google'
        else return 'Login'
      }
    },
    props: {
      long: {
        type: Boolean,
        default: () => false
      }
    }
}
</script>

<style scoped>
.text-small {
  text-transform: none !important;
  font-size: 1em;
  margin-left: 6px;
}
</style>