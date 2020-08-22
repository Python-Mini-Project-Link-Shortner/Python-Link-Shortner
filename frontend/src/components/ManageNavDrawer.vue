<template>
  <!--
    navigation-drawer는 좌측에 뜨는 메뉴 패널이다
    @property {v-model} 네비게이션 화면에 표시 여부 결정
    @property {clipped} navigation-drawer가 app-bar 밑에 있는지 결정
    @value $vuetify.breakpoint.lgAndUp 브라우저 Large 이상의 사이즈에서 true
    @property {app} 해당 컴포넌트를 애플리케이션 레이아웃의 일부로 지정합니다. content sizing을 동적으로 조정하는데 사용됩니다.
  -->
  <v-navigation-drawer v-model="showDrawer" :clipped="$vuetify.breakpoint.lgAndUp" app>
    <template v-slot:prepend v-if="!$vuetify.breakpoint.lgAndUp">
      <div class="mt-3">
        <HomeLogo></HomeLogo>
      </div>
    </template>

    <!--
      메뉴에 표시될 리스트
      @property {subheader} 메뉴 구분용 타이틀 넣을때 필요합니다
    -->
    <v-list subheader>
      <!-- 메뉴의 타이틀 -->
      <v-subheader>Action1</v-subheader>

      <!-- 표시될 아이템 -->
      <v-list-item v-for="item in drawerSubtitle1ActionList" :key="item.text" @click="close();">
        <v-list-item-icon>
          <v-icon v-text="item.icon"></v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title v-text="item.text"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <!-- 구분줄 -->
      <v-divider></v-divider>
      <!-- 메뉴의 타이틀 -->
      <v-subheader>Action2</v-subheader>

      <!-- 표시될 아이템 -->
      <v-list-item v-for="item in drawerSubtitle2ActionList" :key="item.text" @click="close();">
        <v-list-item-icon>
          <v-icon v-text="item.icon"></v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title v-text="item.text"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <!-- 구분줄 -->
      <v-divider></v-divider>
      <!-- 메뉴의 타이틀 -->
      <v-subheader>Action2</v-subheader>

      <!-- 표시될 아이템 -->
      <v-list-item v-for="item in drawerSubtitle3ActionList" :key="item.text" @click="close();">
        <v-list-item-icon>
          <v-icon v-text="item.icon"></v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title v-text="item.text"></v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <template v-slot:append>
      <div class="mb-3">@2020 MiniPy.com</div>
    </template>
  </v-navigation-drawer>
</template>

<script>
import { mapActions } from 'vuex'
import Logo from '@/components/Logo.vue'

export default {
  name: 'ManageNavDrawer',
  components: {
    HomeLogo: Logo
  },
  data: () => ({
    drawerSubtitle1ActionList: [ // 좌측 링크 메뉴1
      { icon: 'mdi-contacts', text: 'Something1', link: '' },
      { icon: 'mdi-history', text: 'Something2', link: '' }
    ],
    drawerSubtitle2ActionList: [ // 좌측 링크 메뉴2
      { icon: 'mdi-content-copy', text: 'Something3', link: '' }
    ],
    drawerSubtitle3ActionList: [ // 좌측 링크 메뉴3
      { icon: 'mdi-content-copy', text: 'Something4', link: '' }
    ]
  }),
  computed: {
    showDrawer: {
      get() { return this.$store.state.manage.showDrawer; }, // Vuex의 manageModule에서 showDrawer 가져옴
      set(value) { if (value === false) this.close(); }
    }
  },
  methods: {
    ...mapActions('manage', [
      'closeDrawer' // vuex의 manageModule에서 함수들 가져옴
    ]),
    close() {
      // Display 크기가 large 이상이 아닐 경우에만 실행됩니다
      if (this.$vuetify.breakpoint.lgAndUp !== true) {
        this.closeDrawer();
      }
    }
  }
}
</script>

<style scoped>

</style>