<template>
  <v-container class="text-left" px-6 py-5 fluid>
    <!-- 링크 트리 -->
    <v-breadcrumbs :items="breadcrumbs.tag" class="pl-2 pt-2 pb-0">
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
      태그관리
    </p>

    <v-row v-for="(tagObj, index) in tagList" :key="tagObj.name" class="mb-4" :class="'scroll' + index">
      <v-col cols="12">
        <v-card hover>
          <div class="card-head" @click="toggleTag(tagObj)">
            <div class="text-h6">#{{ tagObj.name }}</div>
            <v-spacer></v-spacer>
            <v-icon>{{ tagObj.open ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
          </div>
          <v-expand-transition>
            <div class="card-body" v-show="tagObj.open">
              <v-divider></v-divider>
              <div v-for="link in tagObj.linkList" :key="link._id">
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
                  <v-btn class="mr-2 success" @click.stop="diagChange = true; clickedTagObj = tagObj; changeClickedLinkID(link._id)">변경</v-btn>
                  <v-btn class="error" @click.stop="diagDelete = true; clickedTagObj = tagObj; changeClickedLinkID(link._id)">삭제</v-btn>
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
        <v-card-title class="headline">태그변경</v-card-title>
        <v-card-text class="pb-0">
          <v-text-field v-model="changeName" label="태그" hint="변경하고 싶은 태그를 입력하세요"></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="success" text class="font-weight-bold" :disabled="changeName == ''" @click="diagChange = false; changeTagName(changeName)">변경</v-btn>
          <v-btn color="warning" text class="font-weight-bold" @click="diagChange = false;">취소</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- 삭제 Dialog -->
    <v-dialog v-model="diagDelete" width="420">
      <v-card>
        <v-card-title class="headline">태그삭제</v-card-title>
        <v-card-text class="pb-0">
          태그를 지우시면 태그로 검색이 불가능합니다.<br/>
          태그를 지우시겠습니까?
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
  name: 'ManageTag',
  components: {
    Loading: LoadingOverlay,
    Error: ErrorAlert
  },
  data: () => ({
    tagList: [],        // 태그 오브젝트 배열 ({open:bool, name:string, linkList:array}로 구성)
    diagChange: false,  // 태그 변경 다이얼로그 
    diagDelete: false,  // 태그 삭제 다이얼로그
    changeName: '',     // 변경할 태그 이름
    clickedTagObj: {}   // 현재 클릭한 태그 오브젝트
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
      this.diagChange = false
      this.diagDelete = false
      this.changeName = ''
      this.clickedTagObj = {}
      this.changeRequestMode(this.RequestMode.Single)
      this.clearSelectLink()
      this.hideError()
      this.fetchTagList()
    },
    // 내 아이디의 태그 종류 가져오기
    fetchTagList() {
      this.startLoading()

      this.tagList = []
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
    // 내 아이디의 태그 종류 가져오기 및 태그 이름으로 열기
    fetchTagListWithName(openName) {
      this.startLoading()

      this.tagList = []
      axios.post(this.serverURL.tagListURL,
        { userID: this.userInfo.email })
        .then(res => {
          res.data.tags.forEach((item, index, arrSrc) => {
            this.tagList.push({ open: false, name: item, linkList: [] })
          })
        }).catch(e => {
          this.showError('불러오기에 실패하였습니다')
        }).finally(() => {
          const index = this.tagList.findIndex((item) => { return item.name === openName })
          if (index > -1) {
            this.toggleTag(this.tagList[index], true, index)
          } else {
            this.delayedStopLoading()
          }
        })
    },
    // scroll<index> 클래스로 스크롤 이동
    scrollTo(index) {
      this.$vuetify.goTo('.scroll' + index, { duration: 300, offset: 0 })
    },
    // 태그박스 토글
    toggleTag(tagObj, scroll, index) {
      // 토글
      tagObj.open = !tagObj.open

      // 열렸을경우
      if (tagObj.open == true) {
        // 스크롤 있을경우 스크롤 이동
        if (scroll === true) {
          this.fetchTaggedLinkList(tagObj, index)
        } else {
          this.fetchTaggedLinkList(tagObj)
        }
      }
    },
    // 태그에 속한 link 리스트로 가져오기
    fetchTaggedLinkList(tagObj, index) {
      this.startLoading()

      axios.post(this.serverURL.taggedLinkListURL,
        { userID: this.userInfo.email, tag: tagObj.name })
        .then(res => {
          tagObj.linkList = res.data.link
        }).catch(e => {
          this.showError('태그로 불러오기에 실패하였습니다')
        }).finally(() => {
          // index가 있을경우 scroll<index>로 스크롤 이동
          if (index) {
            this.scrollTo(index)
          }
          this.stopLoading()
        })
    },
    changeTagName(name) {
      this.startLoading()

      // 동일한 태그 이름으로 변경시 무시
      if (name == this.clickedTagObj.name)
      {
        this.stopLoading()
        return
      }

      axios.post(this.serverURL.changeTagURL,
        { userID: this.userInfo.email, changeID: this.linkID, tagName: name })
        .then(res => {
          // 리스트에서 삭제
          // const index = this.clickedTagObj.linkList.findIndex((item) => { return item._id === this.linkID[0] })
          // if (index > -1) { this.clickedTagObj.linkList.splice(index, 1) }
        }).catch(e => {
          this.showError("태그 변경에 실패하였습니다")
        }).finally(() => {
          this.clearSelectLink()
          this.changeName = ''

          // 원래 열어둔 곳 저장
          const prevOpenedName = this.clickedTagObj.name
          this.clickedTagObj = {}
          // 페이지 다시 불러오기
          this.fetchTagListWithName(prevOpenedName)
        })
    },
    deleteLink(linkID) {
      this.startLoading()

      axios.post(this.serverURL.deleteLinkURL,
        { userID: this.userInfo.email, deleteID: linkID })
        .then(res => {

        }).catch(e => {
          this.showError("태그 삭제에 실패하였습니다")
        }).finally(() => {
          this.clearSelectLink()
          
          // 원래 열어둔 곳 저장
          const prevOpenedName = this.clickedTagObj.name
          this.clickedTagObj = {}
          // 페이지 다시 불러오기
          this.fetchTagListWithName(prevOpenedName)
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