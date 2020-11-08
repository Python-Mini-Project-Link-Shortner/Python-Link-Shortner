<template>
  <v-container class="text-left" px-6 py-5 fluid>
    <!-- 링크 트리 -->
    <v-breadcrumbs :items="breadcrumbs.tag" class="pl-2 pt-2 pb-0"></v-breadcrumbs>

    <!-- 로딩 -->
    <Loading></Loading>

    <!-- 에러 -->
    <v-row>
      <v-col cols="12">
        <Error></Error>
      </v-col>
    </v-row>

    <p class="text-h4 mb-8 pl-1">
      태그관리
    </p>

    <v-row v-for="tag in tagList" :key="tag.name">
      <v-col cols="12">
        <v-card hover class="">
          <div style="display: flex" @click="tag.open = !tag.open; if (tag.open) { fetchTaggedLinkList(tag) }">
            <div class="text-h6">{{ tag.name }}</div>
            <v-spacer></v-spacer>
            <v-icon>{{ tag.open ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
          </div>
          <v-expand-transition>
            <div v-show="tag.open">
              <v-divider></v-divider>
              <div v-for="link in tag.linkList" :key="link._id" style="display: flex">
                  {{ link.shortURL }}
                  <v-spacer></v-spacer>
                  <v-btn>변경</v-btn>
                  <v-btn>삭제</v-btn>
                </div>
            </div>
          </v-expand-transition>
        </v-card>
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
  name: 'ManageTag',
  components: {
    Loading: LoadingOverlay,
    Error: ErrorAlert
  },
  data: () => ({
    tagList: []    // 태그 배열
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
    ...mapActions('manage', ['startLoading', 'delayedStopLoading', 'stopLoading',
      'showError', 'hideError', 'changeClickedLinkID', 'changeRequestMode', 'clearSelectLink']),
    pageEnter() {
      this.tagList = []
      this.clearSelectLink()
      this.hideError()
      this.fetchTagList()
    },
    fetchTagList() {
      this.startLoading()

      axios.post(this.serverURL.tagListURL,
        { userID: this.userInfo.email })
        .then(res => {
          res.data.tags.forEach((item, index, arrSrc) => {
            this.tagList.push({ open: false, name: item, linkList: [] })
          })
        }).catch(e => {
          this.showError('불러오기에 실패하였습니다')
        }).finally(() => {
          this.delayedStopLoading()
        })
    },
    fetchTaggedLinkList(tagObj) {
      this.startLoading()

      axios.post(this.serverURL.taggedLinkListURL,
        { userID: this.userInfo.email, tag: tagObj.name })
        .then(res => {
          tagObj.linkList = res.data.link
        }).catch(e => {
          this.showError('태그로 불러오기에 실패하였습니다')
        }).finally(() => {
          this.stopLoading()
        })
    }
  }
}
</script>

<style>

</style>