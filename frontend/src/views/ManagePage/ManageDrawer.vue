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
    -->
    <v-list nav dense rounded>
      <div v-for="(drawerItem, index) in drawerManageList" :key="drawerItem.title">
        <v-subheader v-text="drawerItem.title" class="mb-2">
        </v-subheader>

        <!-- <v-list-item v-for="linkItem in drawerItem" :key="linkItem.text" @click="close()"> -->
        <v-list-item v-for="linkItem in drawerItem.linkList" :key="linkItem.text" :to="linkItem.link"
        color="info" v-ripple="{ class: 'blue--text' }" class="nav-info">
          <v-list-item-icon>
            <v-icon v-text="linkItem.icon"></v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title v-text="linkItem.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-divider v-if="index !== drawerManageList.length - 1"></v-divider>
      </div>
    </v-list>

    <template v-slot:append>
      <div class="py-3">@2020 MiniPy.com</div>
    </template>

    <!-- TODO: Logout 버튼 화면 크기에 따라서 여기로 옮기기 -->
  </v-navigation-drawer>
</template>

<script>
import { mapActions } from 'vuex'
import Logo from '@/components/Logo.vue'

export default {
  name: 'ManageDrawer',
  components: {
    HomeLogo: Logo
  },
  data: () => ({
    drawerManageList: [
      { title: '링크관리', linkList: [
        { icon: 'mdi-home', text: '홈페이지', link: '#' },
        { icon: 'mdi-heart', text: '즐겨찾기', link: '#' },
        { icon: 'mdi-tag', text: '태그관리', link: '#' },
        { icon: 'mdi-eye-off', text: '숨김관리', link: '#' },
        { icon: 'mdi-restore-alert', text: '링크검사', link: '#' }
      ]},
      { title: '링크분석', linkList: [
        { icon: 'mdi-chart-areaspline-variant', text: '분석현황', link: '#' },
        { icon: 'mdi-finance', text:'기간별분석', link: '#' },
        { icon: 'mdi-chart-bubble', text: '국가별분석', link: '#' }
      ]},
      {
        title: 'API', linkList: [
          { icon: 'mdi-code-json', text: '메뉴얼', link: '#' }
        ]
      },
      {
        title: '언어', linkList: [
          { icon: 'mdi-translate', text:'ENG', link: '#' },
          { icon: 'mdi-translate', text: '한국어', link: '#' },
          { icon: 'mdi-translate', text: '中文', link: '#' }
        ]
      },
      { title: 'MiniPy', linkList: [
        { icon: 'mdi-chat', text: '연락', link: '#' },
        { icon: 'mdi-file-document-edit', text: '약관', link: '#' },
        { icon: 'mdi-alert-box', text: '신고', link: '#' }
      ]}
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
  .nav-info:hover {
    background-color: #E3F2FD;
  }
  .nav-info:hover * {
    color: #2962FF;
  }
</style>