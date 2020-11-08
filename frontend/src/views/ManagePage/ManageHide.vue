<template>
  <v-container class="text-left" px-6 py-5 fluid>
    <!-- 링크 트리 -->
    <v-breadcrumbs :items="breadcrumbs.hide" class="pl-2 pt-2 pb-0"></v-breadcrumbs>

    <!-- 로딩 -->
    <Loading></Loading>

    <!-- 에러 -->
    <v-row>
      <v-col cols="12">
        <Error></Error>
      </v-col>
    </v-row>

    <p class="text-h4 mb-8 pl-1">
      숨김관리
    </p>
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
    linkList: []    // 링크 배열
  }),
  created: function() {
    this.pageEnter()
  },
  watch: {
    // 라우트 변경시 데이터 가져오기 다시 호출
    '$route': 'pageEnter'
  },
  computed: {
    ...mapState(['serverURL', 'userInfo']),
    ...mapState('manage', ['RequestMode', 'breadcrumbs']),
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