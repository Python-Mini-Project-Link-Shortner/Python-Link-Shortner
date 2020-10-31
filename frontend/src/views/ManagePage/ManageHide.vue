<template>
  <v-container class="text-left" px-6 py-5 fluid>
    <!-- 로딩 -->
    <Loading></Loading>

    <!-- 에러 -->
    <v-row>
      <v-col cols="12">
        <Error></Error>
      </v-col>
    </v-row>

    <p class="text-h4 text-center">
      숨겨진 페이지
    </p>



    <!-- 페이지네이션 -->
    <v-row>
      <v-col cols="12">
        <v-pagination v-model="page" prev-icon="mdi-menu-left" next-icon="mdi-menu-right" :length="maxPage" :page="page" :total-visible="10"></v-pagination>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import axios from 'axios'
import LoadingOverlay from '@/components/Manage/LoadingOverlay.vue'
import ErrorAlert from '@/components/Manage/ErrorAlert.vue'

export default {
  name: 'ManageHide',
  components: {
    Loading: LoadingOverlay,
    Error: ErrorAlert
  },
  data: () => ({
    maxPage: 1, // 최대 페이지
    page: 1,    // 현재 페이지
    itemPerPage: 10, // 페이지 당 아이템 갯수
    linkList: []    // 링크 배열
  }),
  created: function() {
    this.pageEnter()
  },
  watch: {
    // 라우트 변경시 데이터 가져오기 다시 호출
    '$route': 'pageEnter',
    // 페이지 변경시 다음 페이지 데이터 가져오기
    page: function() {
      this.pageEnter()
    }
  },
  computed: {
    ...mapState(['serverURL', 'userInfo']),
    ...mapState('manage', ['RequestMode']),
    ...mapGetters('manage', ['linkID'])
  },
  methods: {
    ...mapActions('manage', ['startLoading', 'delayedStopLoading', 'showError', 'hideError',
      'changeClickedLinkID', 'changeRequestMode', 'clearSelectLink']),
    pageEnter() {
      this.linkList = []
      this.clearSelectLink()
      this.hideError()
    }
  }
}
</script>

<style>

</style>