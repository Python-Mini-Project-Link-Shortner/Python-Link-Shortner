<template>
  <v-container class="text-left" px-6 py-5 fluid>
    <!-- 링크 트리 -->
    <v-breadcrumbs :items="breadcrumbs.favorite" class="pl-2 pt-2 pb-0"></v-breadcrumbs>

    <!-- 로딩 -->
    <Loading></Loading>

    <!-- 에러 -->
    <v-row>
      <v-col cols="12">
        <Error></Error>
      </v-col>
    </v-row>

    <p class="text-h4 mb-8 pl-1">
      즐겨찾기
    </p>

    <v-row v-for="link in linkList" :key="link._id">
      <v-col cols="12">
        <v-card outlined hover class="px-4 py-2">
          <div style="display: flex" >
              <div class="text-h6 text-truncate info--text">
                {{ link.shortURL }}
              </div>
              <v-spacer></v-spacer>
              <div class="pt-1 grey--text">
                {{ link.makeDate }}
              </div>
          </div>
          <div style="display: flex" class="mt-4">
            <div>
              <div class="font-weight-regular text-caption grey--text">{{ link.pageTitle }}</div>
              {{ link.rawURL }}
            </div>
            <v-spacer></v-spacer>
            <div>
              <v-btn style="height: 100%" color="error" class="text-subtitle-1" @click="openDialog(link._id)">취소</v-btn>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>

    <!-- 페이지네이션 -->
    <v-row>
      <v-col cols="12">
        <v-pagination v-model="page" prev-icon="mdi-menu-left" next-icon="mdi-menu-right" :length="maxPage" :page="page" :total-visible="10"></v-pagination>
      </v-col>
    </v-row>

    <v-dialog v-model="removeDialog" width="360">
      <v-card>
        <v-card-title class="headline">
          즐겨찾기 제거
        </v-card-title>
        <v-card-text class="py-2">
          정말로 즐겨찾기에서 제거하시겠습니까?
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" text class="font-weight-bold" @click="closeDialog(); removeFavorite()">제거</v-btn>
          <v-btn color="warning" text class="font-weight-bold" @click="closeDialog()">취소</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import axios from 'axios'
import LoadingOverlay from '@/components/Manage/LoadingOverlay.vue'
import ErrorAlert from '@/components/Manage/ErrorAlert.vue'

export default {
  name: 'ManageFavorite',
  components: {
    Loading: LoadingOverlay,
    Error: ErrorAlert
  },
  data: () => ({
    maxPage: 1, // 최대 페이지
    page: 1,  // 현재 페이지
    itemPerPage: 10, // 페이지 당 아이템 갯수
    linkList: [], // 링크 배열
    removeDialog: false  // 즐겨찾기 제거 시 Dialog 표시상태
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
    ...mapState('manage', ['RequestMode', 'breadcrumbs']),
    ...mapGetters('manage', ['linkID'])
  },
  methods: {
    ...mapActions('manage', ['startLoading', 'delayedStopLoading', 'showError', 'hideError',
      'changeClickedLinkID', 'changeRequestMode', 'clearSelectLink']),
    // 페이지 변경시 호출되어야 할 함수
    pageEnter() {
      this.linkList = []
      this.clearSelectLink()
      this.hideError()
      this.fetchLinkData()
    },
    // Favorite Link 데이터 가져오기
    fetchLinkData() {
      this.startLoading()

      axios.post(this.serverURL.favoritePageURL,
        { userID: this.userInfo.email, page: this.page, itemCount: this.itemPerPage })
        .then(res => {
          this.maxPage = res.data.maxPage
          this.page = res.data.page
          this.linkList = res.data.list
        }).catch(e => {
          this.showError()
        }).finally(() => {
          this.delayedStopLoading()
        })
    },
    openDialog(linkId) {
      if (linkId != null || linkId != '') {
        this.changeClickedLinkID(linkId)
        this.changeRequestMode(this.RequestMode.Single)
        this.removeDialog = true
      } else {
        this.showError('정상적이지 않은 삭제입니다')
      }
    },
    closeDialog() {
      this.removeDialog = false
    },
    removeFavorite() {
      this.startLoading()

      axios.post(this.serverURL.uncheckFavoriteURL,
        { userID: this.userInfo.email, favoriteID: this.linkID })
        .then(res => {
          this.fetchLinkData()
        }).catch(e => {
          this.showError("변경에 실패하였습니다")
        }).finally(() => {
          this.clearSelectLink()
          this.delayedStopLoading()
        })
    }
  }
}
</script>

<style>
.half-width {
  width: 50%;
}
</style>