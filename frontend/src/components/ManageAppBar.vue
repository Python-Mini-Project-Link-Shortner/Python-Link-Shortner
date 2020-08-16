<template>
  <!--
    상단 툴바
    @property {clipped-left} 좌측의 navigation-drawer가 app-bar 밑에 있는지 결정
    @value $vuetify.breakpoint.lgAndUp 브라우저 Large 이상의 사이즈에서 true
    @property {collapse-on-scroll} 스크롤중에는 collapsed 상태로 변경
    @property {app} 해당 컴포넌트를 애플리케이션 레이아웃의 일부로 지정합니다. content sizing을 동적으로 조정하는데 사용됩니다. 
  -->
  <v-app-bar :clipped-left="$vuetify.breakpoint.lgAndUp" app>
    <!-- 메뉴버튼 -->
    <v-app-bar-nav-icon @click.stop="toggleDrawer()"></v-app-bar-nav-icon>
    <!-- 타이틀 -->
    <v-toolbar-title class="toolbar-title ml-0 pl-4 text-left">
      <v-btn depressed tile blocked :ripple="false" class="hidden-xs no-background-hover">
        Link Shortner Title
      </v-btn>
    </v-toolbar-title>
    <!--
      검색바
      @property {flat} solo나 solo-inverted일 때 그림자 비활성화
      @property {solo-inverted} focus 되기 전까지 투명한 상태로 활성화
      @property {hide-details} 메뉴 위에 있어서 hint가 추가되면 레이아웃 깨지므로 가려준다
      @property {label} 아무 입력도 없을 때 나오는 단어
      @property {prepend-inner-icon} 입력창 내부 좌측에 붙여줄 아이콘. v-icon 참고 
    -->
    <v-text-field flat solo-inverted hide-details label="Keywords" prepend-inner-icon="mdi-magnify" class="hidden-xs"></v-text-field>
    <!-- 공백 채우기 -->
    <v-spacer></v-spacer>
    <v-divider vertical></v-divider>
    <!-- 계정관리 -->
    <v-menu v-model="showAccountMenu" :offset-y="true">
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
          @property {ripple} 물결 이펙트
          @property {v-bind} 슬롯의 attrs로 설정
          @property {v-on} 슬롯의 on으로 설정
        -->
        <v-btn depressed tile :ripple="false" v-bind="attrs" v-on="on" class="no-background-hover max-height">
          My Account <v-icon v-text="showAccountMenu ? 'mdi-chevron-up' : 'mdi-chevron-down'"></v-icon>
        </v-btn>
      </template>

      <!--
        계정관리 메뉴
      -->
      <v-list>
        <v-list-item v-for="(item, index) in accountActionList" :key="'account-action-' + index" @click="">
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-app-bar>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'ManageAppBar',
  data: () => ({
    showAccountMenu: false, // 계정 관리 메뉴 표시 여부
    accountActionList: [ // 관리 메뉴
      { title: '링크관리', link: '' },
      { title: '계정관리', link: '' },
      { title: '로그아웃', link: '' }
    ]
  }),
  methods: {
    ...mapActions('manage', [
      'toggleDrawer'
    ])
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

.max-height {
  height: 100% !important;
}
</style>