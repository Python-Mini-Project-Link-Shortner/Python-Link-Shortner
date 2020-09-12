<template>
  <div>
    <!--
      상단 툴바
      @property {clipped-left} 좌측의 navigation-drawer가 app-bar 밑에 있는지 결정
      @value $vuetify.breakpoint.lgAndUp 브라우저 Large 이상의 사이즈에서 true
      @property {collapse-on-scroll} 스크롤중에는 collapsed 상태로 변경
      @property {app} 해당 컴포넌트를 애플리케이션 레이아웃의 일부로 지정합니다. content sizing을 동적으로 조정하는데 사용됩니다. 
    -->
    <v-app-bar :clipped-left="$vuetify.breakpoint.lgAndUp" class="white" app>

      <!-- 메뉴버튼 -->
      <v-app-bar-nav-icon v-if="!$vuetify.breakpoint.lgAndUp" @click.stop="toggleDrawer()"></v-app-bar-nav-icon>
      <!-- 타이틀 -->
      <v-toolbar-title class="ml-0 pl-4">
        <HomeLogo :to="{name: 'Manage'}"></HomeLogo>
      </v-toolbar-title>
      <!-- 공백 채우기 -->
      <v-spacer></v-spacer>
      
      <!-- 검색 바 -->
      <SearchComp class="hidden-sm-and-down"></SearchComp>

      <!-- 공백 채우기 -->
      <v-spacer></v-spacer>
      <!-- 계정관리 -->
      <v-menu v-model="showAccountMenu" :offset-y="true" transition="slide-y-transition" :close-on-click="true" class="white">
        <!--
          계정관리 버튼 슬롯
          @property {v-slot} 어느 Vue Slot에 넣어줄것인지 정해준다. v-menu는 activator 슬롯만 존재한다
          @values attrs, on, value
          @value on 이벤트
          @value attr attribute 데이터
        -->
        <template v-slot:activator="{ on, attrs }">
          <!--
            계정관리 버튼
            @property {depressed} box-shadow 0으로 설정
            @property {tile} radius 0으로 설정
            @property {v-bind} 슬롯의 attrs로 설정
            @property {v-on} 슬롯의 on으로 설정
          -->
          <!-- TODO: 크기에 따라 drawer로 숢기기 -->
          <v-btn tile v-bind="attrs" v-on="on" class="no-background-hover info pl-3 pr-1 py-5 rounded wd-128 white--text text-subtitle-1 hidden-sm-and-down">
            아이디 <v-icon v-text="showAccountMenu ? 'mdi-chevron-up' : 'mdi-chevron-down'"></v-icon>
          </v-btn>
        </template>

        <!--
          계정관리 메뉴
        -->
        <v-list class="grey lighten-4" nav>
          <v-list-item v-for="(item, index) in accountActionList" :key="'account-action-' + index"
          v-ripple="{ class: 'blue--text' }" 
          class="list-blue" :to="item.link" style="cursor: pointer;">
            <v-list-item-content>
              <v-list-item-title v-text="item.title" 
              @click="accountActionClick(item.action)">
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-menu>

      <!-- TODO: slot을 md-and-down 일때만 표시되게 해보기 -->
      <!-- <template v-slot:extension class="hidden-md-and-up">
        <SearchComp class="hidden-md-and-up"></SearchComp>
      </template> -->
    </v-app-bar>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import Logo from '@/components/Logo.vue'
import SearchBar from '@/components/Manage/SearchBar.vue'
import {userLogout} from '@/assets/js/account.js'

// lgAndUp일때 ManageNavDrawer를 항상 보여주게 된다
export default {
  name: 'ManageNavBar',
  components: {
    HomeLogo: Logo,
    SearchComp: SearchBar
  },
  mounted() {
    // 크기 줄이고 뒤로가기 후 다시 돌아올 때 문제생기므로 여기서 처리해줘야한다
    if (this.$vuetify.breakpoint.lgAndUp === true) {
      this.openDrawer();
    }
  },
  data: () => ({
    showAccountMenu: false, // 계정 관리 메뉴 표시 여부
    accountActionList: [ // 관리 메뉴
      { title: '계정관리', link: '', event: ''},
      { title: '로그아웃', link: '', action: 'logout'}
    ]
  }),
  methods: {
    ...mapActions('manage', [
      'toggleDrawer', 'openDrawer'
    ]),
    accountActionClick(action) {
      if (action === 'logout') {
        userLogout()
      }
    }
  }
}
</script>

<style scoped>

/deep/ .v-toolbar__content {
  padding-top: 0px !important;
  padding-bottom: 0px !important;
  padding-right: 12px !important;
}

.toolbar-title {
  width: 300px;
}

.no-background-hover::before {
  background-color: transparent !important;
}

.wd-128 {
  min-width: 128px !important;
}

.list-blue:hover {
  background-color: #E3F2FD;
}
.list-blue:hover * {
  color: #2962FF;
}
</style>