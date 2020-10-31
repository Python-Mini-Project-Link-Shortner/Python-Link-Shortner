<template>
  <v-container class="text-left" px-6 py-5 fluid>
    <!-- 로딩창 -->
    <Loading></Loading>

    <!-- 분석창 -->
    <v-row>
      <v-col cols="12">
        <div
          class="grey lighten-4"
          style="height: 240px; border-radius: 8px;"
        >
          
        </div>
      </v-col>
    </v-row>

    <!-- Link Shortner 입력창 -->
    <v-row>
      <v-col cols="12">
        <LinkInput alert></LinkInput>
      </v-col>
    </v-row>

    <!-- 오류 -->
    <v-row>
      <v-col cols="12">
        <Error></Error>
      </v-col>
    </v-row>

    <!-- 링크 -->
    <v-row v-for="link in linkList" :key="link._id">
      <v-col cols="12">
        <v-card outlined hover>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="text-h6 text-truncate info--text">{{ link.shortURL }}</v-list-item-title>
              <v-list-item-subtitle>{{ link.makeDate }}</v-list-item-subtitle>
            </v-list-item-content>
            <v-spacer></v-spacer>
            <v-checkbox v-model="checkedLinkIDList" :value="link._id"></v-checkbox>
          </v-list-item>

          <v-card-subtitle class="py-0 font-weight-regular">브라우저탭에뜨는 이름</v-card-subtitle>
          <v-card-text class="text--primary pb-1">{{ link.rawURL }}</v-card-text>

          <v-card-actions class="px-4">
            <!-- 태그 표시 -->
            <div>
              <v-chip color="info" text-color="white" v-if="link.tagName">#{{ link.tagName }}</v-chip>
              <v-chip v-else>####</v-chip>
            </div>

            <v-spacer></v-spacer>

            <!-- Dialog 버튼 -->
            <v-tooltip top>
              <template v-slot:activator="{ on, attrs }">
                <v-btn icon dark color="success" v-bind="attrs" v-on="on" @click.stop="openDialog(DialogName.Favorite, RequestMode.Single, link._id)">
                  <v-icon v-if="link.favorite">mdi-heart</v-icon>
                  <v-icon v-else>mdi-heart-outline</v-icon>
                </v-btn>
              </template>
              <span>즐겨찾기</span>
            </v-tooltip>
            <v-tooltip top>
              <template v-slot:activator="{ on, attrs }">
                <v-btn icon dark color="info" v-bind="attrs" v-on="on" @click.stop="openDialog(DialogName.Tag, RequestMode.Single, link._id);">
                  <v-icon>mdi-tag-outline</v-icon>
                </v-btn>
              </template>
              <span>태그변경</span>
            </v-tooltip>
            <v-tooltip top>
              <template v-slot:activator="{ on, attrs }">
                <v-btn icon dark color="warning" v-bind="attrs" v-on="on" @click.stop="openDialog(DialogName.Hide, RequestMode.Single, link._id);">
                  <v-icon>mdi-eye-off-outline</v-icon>
                </v-btn>
              </template>
              <span>숨기기</span>
            </v-tooltip>
            <v-tooltip top>
              <template v-slot:activator="{ on, attrs }">
                <v-btn icon dark color="error" v-bind="attrs" v-on="on" @click.stop="openDialog(DialogName.Delete, RequestMode.Single, link._id);">
                  <v-icon>mdi-delete-outline</v-icon>
                </v-btn>
              </template>
              <span>링크삭제</span>
            </v-tooltip>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <!-- 페이지네이션 -->
    <v-row>
      <v-col cols="12">
        <v-pagination v-model="page" prev-icon="mdi-menu-left" next-icon="mdi-menu-right" :length="maxPage" :page="page" :total-visible="10"></v-pagination>
      </v-col>
    </v-row>

    <!-- Floating Button -->
    <v-speed-dial v-model="fab" fixed right bottom :transition="'slide-y-reverse-transition'">
      <template v-slot:activator>
        <v-btn v-model="fab" fab dark color="pink darken-1">
          <v-icon v-if="fab">mdi-close</v-icon>
          <v-icon v-else>mdi-plus</v-icon>
        </v-btn>
      </template>
      <v-tooltip left>
        <template v-slot:activator="{ on, attrs }">
          <v-btn fab dark small color="error" v-bind="attrs" v-on="on" :disabled="fabDisabled" @click.stop="openDialog(DialogName.Delete, RequestMode.Multiple)">
            <v-icon>mdi-delete</v-icon>
          </v-btn>
        </template>
        <span>선택한 링크들을 삭제합니다</span>
      </v-tooltip>
      <v-tooltip left>
        <template v-slot:activator="{ on, attrs }">
          <v-btn fab dark small color="warning" v-bind="attrs" v-on="on" :disabled="fabDisabled" @click.stop="openDialog(DialogName.Hide, RequestMode.Multiple)">
            <v-icon>mdi-eye-off</v-icon>
          </v-btn>
        </template>
        <span>선택한 링크들을 숨깁니다</span>
      </v-tooltip>
      <v-tooltip left>
        <template v-slot:activator="{ on, attrs }">
          <v-btn fab dark small color="info" v-bind="attrs" v-on="on" :disabled="fabDisabled" @click.stop="openDialog(DialogName.Tag, RequestMode.Multiple)">
            <v-icon>mdi-tag</v-icon>
          </v-btn>
        </template>
        <span>선택한 링크들의 태그를 변경합니다</span>
      </v-tooltip>
      <v-tooltip left>
        <template v-slot:activator="{ on, attrs }">
          <v-btn fab dark small color="success" v-bind="attrs" v-on="on" :disabled="fabDisabled" @click.stop="openDialog(DialogName.Favorite, RequestMode.Multiple)">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
        </template>
        <span>선택한 링크들의 즐겨찾기를 변경합니다</span>
      </v-tooltip>
    </v-speed-dial>

    <!-- Dialog 모음 -->
    <div>
      <!-- 즐겨찾기 Dialog -->
      <v-dialog v-model="dialogs.favoriteOpen" width="360">
        <v-card>
          <v-card-title class="headline">
            즐겨찾기
            <v-spacer></v-spacer>
            <v-btn color="error" icon class="font-weight-bold" @click="closeDialog(DialogName.Favorite)">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-card-title>
          <v-card-text class="pb-0">
            즐겨찾기를 변경하시겠습니까?
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="success" text class="font-weight-bold" @click="closeDialog(DialogName.Favorite); changeFavorite(true);">
              추가
            </v-btn>
            <v-btn color="error" text class="font-weight-bold" @click="closeDialog(DialogName.Favorite); changeFavorite(false);">
              제거
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- 태그 Dialog -->
      <v-dialog v-model="dialogs.tagOpen" max-width="420">
        <v-card>
          <v-card-title class="headline">
            태그
            <v-spacer></v-spacer>
            <v-btn color="error" icon class="font-weight-bold" @click="closeDialog(DialogName.Tag); tagMode = TagMode.None">
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-card-title>
          <v-card-text class="pb-0">
            <v-row v-if="tagMode == TagMode.None">
              <v-col cols="6">
                <v-btn color="success" class="full-width" @click="tagMode = TagMode.Change;">
                  태그 변경
                </v-btn>
              </v-col>
              <v-col cols="6">
                <v-btn color="error" class="full-width" @click="tagMode = TagMode.Delete;">
                  태그 삭제
                </v-btn>
              </v-col>
            </v-row>
            <v-row v-if="showTagChange">
              <v-col class="my-0 pb-0">
                <v-text-field label="원하는 태그를 입력하세요" v-model="tagName" class="mt-0 pt-0"></v-text-field>
              </v-col>
            </v-row>
            <v-row v-if="showTagChange">
              <v-col cols="6">
                <v-btn color="success" class="full-width" :disabled="tagName == ''" @click="closeDialog(DialogName.Tag); changeTag(tagName)">
                  변경
                </v-btn>
              </v-col>
              <v-col cols="6">
                <v-btn color="warning" class="full-width" @click="tagMode = TagMode.None">
                  취소
                </v-btn>
              </v-col>
            </v-row>
            <v-row v-if="showTagDelete">
              <v-col>
                <v-container class="pt-0 text-subtitle-1 font-weight-medium black--text">
                  태그를 지우시면 태그로 검색이 불가능합니다.<br/>
                  태그를 지우시겠습니까?
                </v-container>
              </v-col>
            </v-row>
            <v-row v-if="showTagDelete">
              <v-col cols="6">
                <v-btn color="error" class="full-width" @click="closeDialog(DialogName.Tag); deleteTag()">
                  확인
                </v-btn>
              </v-col>
              <v-col cols="6">
                <v-btn color="warning" class="full-width" @click="tagMode = TagMode.None">
                  취소
                </v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-dialog>

      <!-- 숨김 Dialog -->
      <v-dialog v-model="dialogs.hideOpen" max-width="360">
        <v-card>
          <v-card-title class="headline">
            링크 숨기기
          </v-card-title>
          <v-card-text class="pb-0">
            원하는 위치를 고르세요<br/>
            <v-select v-model="hideName" :items="hideNameList" :menu-props="{ offsetY: true }"></v-select>
            <v-btn @click="fetchHideList()">불러오기</v-btn>
            <v-text-field v-model="hideName" label="숨길 위치" hint="직접 입력도 가능해요"></v-text-field>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="success" text class="font-weight-bold" :disabled="hideName == ''" @click="closeDialog(DialogName.Hide); hideLink(hideName);">
              숨기기
            </v-btn>
            <v-btn color="warning" text class="font-weight-bold" @click="closeDialog(DialogName.Hide)">
              취소
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <!-- 삭제 Dialog -->
      <v-dialog v-model="dialogs.deleteOpen" max-width="360">
        <v-card>
          <v-card-title class="headline error--text">
            링크 삭제
          </v-card-title>
          <v-card-text class="pb-0">
            해당 작업은 되돌릴 수 없습니다.<br/>
            정말로 삭제하시겠습니까?
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="error" text class="font-weight-bold" @click="closeDialog(DialogName.Delete); deleteLink();">
              삭제
            </v-btn>
            <v-btn color="warning" text class="font-weight-bold" @click="closeDialog(DialogName.Delete)">
              취소
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </v-container>
</template>

<script>
import { mapState, mapActions, mapGetters } from 'vuex'
import axios from 'axios'
import ShortenLink from '@/components/ShortenLink.vue'
import LoadingOverlay from '@/components/Manage/LoadingOverlay.vue'
import ErrorAlert from '@/components/Manage/ErrorAlert.vue'

// enum value
const DialogName = Object.freeze({
  Favorite: Symbol("Favorite"),
  Delete: Symbol("Delete"),
  Hide: Symbol("Hide"),
  Tag: Symbol("Tag")
})

const TagMode = Object.freeze({
  Change: Symbol("Change"),
  Delete: Symbol("Delete"),
  None: Symbol("None")
})

export default {
  name: 'ManageHome',
  components: {
    LinkInput: ShortenLink,
    Loading: LoadingOverlay,
    Error: ErrorAlert
  },
  data: () => ({
    DialogName,
    TagMode,
    maxPage: 1, // 최대 페이지 번호
    page: 1, // 현재 페이지 번호
    itemPerPage: 10, // 페이지 당 아이템 갯수
    fab: false, // Floating Button 클릭 상태
    dialogs: {
      favoriteOpen: false,
      deleteOpen: false,
      hideOpen: false,
      tagOpen: false
    },
    linkList: [], // 링크 정보 배열
    tagMode: TagMode.None, // 태그 요청 모드
    tagName: '', // 태그 변경시 사용자가 입력한 태그 이름이 저장될 공간
    hideNameList: [], // 링크 숨긴 위치들이 저장된 배열
    hideName: '', // 링크를 숨길 위치 이름
  }),
  created: function() {
    // 생성되었을 때 데이터 가져오기
    this.pageEnter()
  },
  watch: {
    // 라우트 변경시 데이터 가져오기 다시 호출
    '$route': 'pageEnter',
    // 페이지 변경시 다음 페이지 데이터 가져오기
    page: function() {
      this.pageEnter()
    },
    // dialog 변경시마다 체크할 값들 검사
    dialogs: {
      deep: true,
      handler(newObj) {
        // tag mode는 열릴때마다 초기화되어야 한다
        if (newObj.tagOpen == true) {
          this.tagMode = TagMode.None
        }
      }
    }
  },
  computed: {
    ...mapState(['serverURL', 'userInfo']),
    ...mapState('manage', ['RequestMode']),
    ...mapGetters('manage', ['linkID']),
    showTagChange: function() {
      switch (this.tagMode) {
      case this.TagMode.Change:
        return true
      default:
        return false
      }
    },
    showTagDelete: function() {
      switch (this.tagMode) {
      case this.TagMode.Delete:
        return true
      default:
        return false
      }
    },
    checkedLinkIDList: {
      get() { return this.$store.state.manage.checkedLinkIDList },
      set(value) { this.changeCheckedLinkIDList(value) }
    },
    fabDisabled: function() {
      return this.checkedLinkIDList.length === 0
    }
  },
  methods: {
    ...mapActions('manage',
      ['clearSelectLink', 'changeClickedLinkID', 'changeCheckedLinkIDList', 'changeRequestMode',
        'startLoading', 'delayedStopLoading', 'showError', 'hideError']),
    // 페이지 변경전 Vue 초기화
    resetForPaging() {
      this.fab = false
      this.linkList.length = 0
      this.clearSelectLink(),
      this.tagMode = this.TagMode.None
      this.tagName = ''
      this.hideNameList.length = 0
      this.hideName = ''
      this.hideError()
    },
    // 페이지가 변경될 때마다 호출된다
    pageEnter() {
      this.resetForPaging()
      this.fetchLinkData()
    },
    // 자신의 아이디에 해당하는 LinkList를 서버에서 가져온다
    fetchLinkData() {
      this.startLoading()

      axios.post(this.serverURL.linkPageURL,
        { userID: this.userInfo.email, page: this.page, itemCount: this.itemPerPage })
        .then(res => {
          this.maxPage = res.data.maxPage
          this.page = res.data.page
          this.linkList = res.data.list
        }).catch(e => {
          this.showError("데이터 불러오기에 실패하였습니다")
        }).finally(() => {
          this.delayedStopLoading()
        })
    },
    // 나의 링크 숨김 위치들을 가져온다
    fetchHideList() {
      this.startLoading()

      axios.post(this.serverURL.hideNameListURL,
        { userID: this.userInfo.email })
        .then(res => {
          this.hideNameList = res.data.filter(function(data) {
            return (data != null && data != '')
          })
        }).catch(e => {
          this.showError("숨김 위치 목록을 불러오는데 실패하였습니다")
        }).finally(() => {
          this.delayedStopLoading()
        })
    },
    // Dialog 열기
    openDialog(dialogName, requestMode, linkId = '') {
      // linkId 제공될경우 요청한 것으로 변경
      if (linkId !== '') {
        this.changeClickedLinkID(linkId)
      }
      
      // RequestMode 변경
      this.changeRequestMode(requestMode)

      // Dialog 변경
      this.changeDialogValue(dialogName, true)
    },
    // Dialog 닫기
    closeDialog(dialogName) {
      this.changeDialogValue(dialogName, false)
    },
    // Dialog들을 Enum으로 관리할 때 값 변경을 위한 함수
    changeDialogValue(dialogName, value = true) {
      switch (dialogName) {
      case this.DialogName.Favorite:
        this.dialogs.favoriteOpen = value
        break
      case this.DialogName.Delete:
        this.dialogs.deleteOpen = value
        break
      case this.DialogName.Hide:
        this.dialogs.hideOpen = value
        break
      case this.DialogName.Tag:
        this.dialogs.tagOpen = value
        break
      case this.DialogName.TagChange:
        this.dialogs.tagChangeOpen = value
        break
      default:
        this.dialogs.tagDeleteOpen = value
        break
      }
    },
    // Card에서 Delete 버튼 클릭시 실행될 링크 지우는 함수
    deleteLink() {
      this.startLoading()

      axios.post(this.serverURL.deleteLinkURL,
        { userID: this.userInfo.email, deleteID: this.linkID })
        .then(res => {
          this.fetchLinkData()
        }).catch(e => {
          this.showError("삭제에 실패하였습니다")
        }).finally(() => {
          this.clearSelectLink()
          this.delayedStopLoading()
        })
    },
    // 선택한 링크의 태그 변경하는 함수
    changeTag(tagName) {
      this.startLoading()

      axios.post(this.serverURL.changeTagURL,
        { userID: this.userInfo.email, changeID: this.linkID, tagName: tagName })
        .then(res => {
          this.fetchLinkData()
        }).catch(e => {
          this.showError("태그 변경에 실패하였습니다")
        }).finally(() => {
          this.clearSelectLink()
          this.tagName = ''
          this.delayedStopLoading()
        })
    },
    // 선택한 링크의 태그 삭제하는 함수
    deleteTag() {
      this.startLoading()

      axios.post(this.serverURL.deleteTagURL,
        { userID: this.userInfo.email, deleteID: this.linkID })
        .then(res => {
          this.fetchLinkData()
        }).catch(e => {
          this.showError("태그 삭제에 실패하였습니다")
        }).finally(() => {
          this.clearSelectLink()
          this.delayedStopLoading()
        })
    },
    // 즐겨찾기 변경
    changeFavorite(favorite) {
      this.startLoading()

      console.log(this.linkID)
      axios.post(favorite == true ? this.serverURL.checkFavoriteURL : this.serverURL.uncheckFavoriteURL,
        { userID: this.userInfo.email, favoriteID: this.linkID })
        .then(res => {
          this.fetchLinkData()
        }).catch(e => {
          this.showError("변경에 실패하였습니다")
        }).finally(() => {
          this.clearSelectLink()
          this.delayedStopLoading()
        })
    },
    // 선택한 링크 숨기기
    hideLink(hideName) {
      this.startLoading()

      axios.post(this.serverURL.hideURL,
        { userID: this.userInfo.email, hideID: this.linkID, hideName: hideName })
        .then(res => {
          this.fetchLinkData()
        }).catch(e => {
          this.showError("숨기기에 실패하였습니다")
        }).finally(() => {
          this.clearSelectLink()
          this.hideName = ''
          this.delayedStopLoading()
        })
    }
  }
}
</script>

<style scoped>
.full-width {
  width: 100%;
}
</style>