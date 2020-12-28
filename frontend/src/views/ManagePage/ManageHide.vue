<template>
  <v-container class="text-left" px-6 py-5 fluid>
    <!-- 링크 트리 -->
    <v-breadcrumbs :items="breadcrumbs.hide" class="pl-2 pt-2 pb-0">
      <template v-slot:item="{ item }">
        <v-breadcrumbs-item
          :to="{ name: item.link }"
          :exact="true">
          {{ item.text }}
        </v-breadcrumbs-item>
      </template>
    </v-breadcrumbs>

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

    <v-row v-for="(hideObj, index) in hideList" :key="hideObj.name" class="mb-4" :class="'scroll' + index">
      <v-col cols="12">
        <v-card hover>
          <div class="card-head" @click="toggleDirectory(hideObj)">
            <div class="text-h6">{{ hideObj.name }}</div>
            <v-spacer></v-spacer>
            <v-icon>{{ hideObj.open ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
          </div>
          <v-expand-transition>
            <div class="card-body" v-show="hideObj.open">
              <v-divider></v-divider>
              <div v-for="link in hideObj.linkList" :key="link._id">
                <div class="card-row-content">
                  <div>
                    <div style="height: 18px;" class="font-weight-regular text-caption grey--text">
                      {{ link.pageTitle ? link.pageTitle : link.rawURL }}
                    </div>
                    <div style="height: 24px;">
                      {{ link.shortURL }}
                    </div>
                  </div>
                  <v-spacer></v-spacer>
                  <v-btn class="mr-2 success" @click.stop="diagChange = true; clickedHideObj = hideObj; changeClickedLinkID(link._id)">변경</v-btn>
                  <v-btn class="error" @click.stop="diagDelete = true; clickedHideObj = hideObj; changeClickedLinkID(link._id)">삭제</v-btn>
                </div>
                <v-divider></v-divider>
              </div>
            </div>
          </v-expand-transition>
        </v-card>
      </v-col>
    </v-row>

    <!-- 변경 Dialog -->
    <v-dialog v-model="diagChange" width="420">
      <v-card>
        <v-card-title class="headline">디렉토리 변경</v-card-title>
        <v-card-text class="pb-0">
          <v-text-field v-model="changeName" label="디렉토리" hint="변경하고 싶은 디렉토리를 입력하세요"></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="success" text class="font-weight-bold" :disabled="changeName == ''" @click="diagChange = false; changeDirectoryName(changeName)">변경</v-btn>
          <v-btn color="warning" text class="font-weight-bold" @click="diagChange = false;">취소</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- 삭제 Dialog -->
    <v-dialog v-model="diagDelete" width="420">
      <v-card>
        <v-card-title class="headline">링크 삭제</v-card-title>
        <v-card-text class="pb-0">
          숨겨진 링크가 다시 보여지게 됩니다.<br/>
          디렉토리에서 삭제하시겠습니까?
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="error" text class="font-weight-bold" @click="diagDelete = false; deleteLink(linkID)">확인</v-btn>
          <v-btn color="warning" text class="font-weight-bold" @click="diagDelete = false;">취소</v-btn>
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
  name: 'ManageHide',
  components: {
    Loading: LoadingOverlay,
    Error: ErrorAlert
  },
  data: () => ({
    hideList: [],       // 숨김 오브젝트 배열
    diagChange: false,  // 변경 다이얼로그
    diagDelete: false,  // 삭제 다이얼로그
    changeName: '',     // 변경할 숨김 디렉토리 이름
    clickedHideObj: {}  // 현재 클릭한 숨김 오브젝트
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
    ...mapActions('manage', ['startLoading', 'stopLoading', 'delayedStopLoading',
      'showError', 'hideError', 'changeClickedLinkID', 'changeRequestMode', 'clearSelectLink']),
    pageEnter() {
      this.diagChange = false
      this.diagDelete = false
      this.changeName = ''
      this.clickedHideObj = {}
      this.changeRequestMode(this.RequestMode.Single)
      this.clearSelectLink()
      this.hideError()
      this.fetchHideList()
    },
    // 숨김 경로 가져오기
    fetchHideList() {
      this.startLoading()

      this.hideList = []
      axios.post(this.serverURL.hideNameListURL,
        { userID: this.userInfo.email })
        .then(res => {
          res.data.list.forEach((item, index, arrSrc) => {
            this.hideList.push({ open: false, name: item, linkList: [] })
          })
        }).catch(e => {
          this.showError('불러오기에 실패하였습니다')
        }).finally(() => {
          this.delayedStopLoading()
        })
    },
    // 숨김 경로 가져오기 및 이름으로 미리 열기
    fetchHideListWithName(openName) {
      this.startLoading()

      this.hideList = []
      axios.post(this.serverURL.hideNameListURL,
        { userID: this.userInfo.email })
        .then(res => {
          res.data.list.forEach((item, index, arrSrc) => {
            this.hideList.push({ open: false, name: item, linkList: [] })
          })
        }).catch(e => {
          this.showError('불러오기에 실패하였습니다')
        }).finally(() => {
          const index = this.hideList.findIndex((item) => { return item.name === openName })
          if (index > -1) {
            this.toggleDirectory(this.hideList[index], true, index)
          } else {
            this.delayedStopLoading()
          }
        })
    },
    // scroll<index> 클래스로 스크롤 이동
    scrollTo(index) {
      this.$vuetify.goTo('.scroll' + index, { duration: 300, offset: 0 })
    },
    // 디렉토리 토글
    toggleDirectory(hiddenObj, scroll, index) {
      // 토글
      hiddenObj.open = !hiddenObj.open

      // 열렸을경우
      if (hiddenObj.open == true) {
        // 스크롤 있을경우 스크롤 이동
        if (scroll === true) {
          this.fetchhiddenLinkList(hiddenObj, index)
        } else {
          this.fetchhiddenLinkList(hiddenObj)
        }
      }
    },
    // 숨김 디렉토리에 속한 link 리스트로 가져오기
    fetchhiddenLinkList(hiddenObj, index) {
      this.startLoading()

      axios.post(this.serverURL.hiddenLinkListURL,
        { userID: this.userInfo.email, directory: hiddenObj.name })
        .then(res => {
          hiddenObj.linkList = res.data.link
        }).catch(e => {
          this.showError('디렉토리로 불러오기에 실패하였습니다')
        }).finally(() => {
          // index가 있을경우 scroll<index>로 스크롤 이동
          if (index) {
            this.scrollTo(index)
          }
          this.stopLoading()
        })
    },
    changeDirectoryName(name) {
      this.startLoading()

      axios.post(this.serverURL.hideURL,
        { userID: this.userInfo.email, hideID: this.linkID, hideName: name })
        .then(res => {

        }).catch(e => {
          this.showError('디렉토리 변경에 실패하였습니다')
        }).finally(() => {
          this.clearSelectLink()
          this.changeName = ''

          // 원래 열어둔 곳 저장
          const prevOpenedName = this.clickedHideObj.name
          this.clickedHideObj = {}
          // 페이지 다시 불러오기
          this.fetchHideListWithName(prevOpenedName)
        })
    },
    deleteLink(linkID) {
      this.startLoading()

      axios.post(this.serverURL.unhideURL,
        { userID: this.userInfo.email, hideID: this.linkID })
        .then(res => {

        }).catch(e => {
          this.showError('삭제에 실패하였습니다')
        }).finally(() => {
          this.clearSelectLink()

          // 원래 열어둔 곳 저장
          const prevOpenedName = this.clickedHideObj.name
          this.clickedHideObj = {}
          // 페이지 다시 불러오기
          this.fetchHideListWithName(prevOpenedName)
        })
    }
  }
}
</script>

<style scoped>
.card-head {
  display: flex;
  padding: 8px 16px;
  background-color: #E1F5FE;
}

.card-body {
  background-color: #FAFAFA;
}

.card-row-content {
  display: flex;
  align-items: center;
  padding: 0px 16px;
  min-height: 60px;
}
</style>