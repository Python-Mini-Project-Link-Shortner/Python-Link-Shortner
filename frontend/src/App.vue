<template>
  <v-app>
    <!--
      네비게이션 용 컴포넌트 만들어서 구분시키든지
      이름 바꿔서 appbar와 navdrawer가 필요한 모듈을 각자 로드하게 바꾸든지
    -->
    <manageAppBar v-if="showManageNav" />
    <manageNavDrawer v-if="showManageNav" />

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
const managePattern = /\/manage.*/;

export default {
  name: 'App',
  computed: {
    showManageNav: function() {
      // vuex에 저장하든지 네비게이션 용 컴포넌트에 옮기던지 해야할듯
      return managePattern.test(this.$route.path);
    }
  },
  components: {
    manageAppBar: () => import('@/components/ManageAppBar.vue'),
    manageNavDrawer: () => import('@/components/ManageNavDrawer.vue')
  }
}
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
