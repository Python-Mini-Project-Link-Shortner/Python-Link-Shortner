<template>
  <v-app>
    <router-view name="navBar"></router-view>
    <router-view name="drawer"></router-view>
    <v-main>
      <router-view />
    </v-main>
    <router-view name="footer"></router-view>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  data: () => ({
    //
  }),
};
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
