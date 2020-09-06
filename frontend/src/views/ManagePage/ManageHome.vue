<template>
  <v-container class="text-left" px-6 py-5 fluid>
    <!-- 로딩창 -->
    <v-overlay :absolute=true :value="loading">
      <v-progress-circular indeterminate size="64"></v-progress-circular>
    </v-overlay>

    <!-- 분석창 -->
    <v-row>
      <v-col cols="12">
        <div style="height: 240px; border: 1px solid black; border-radius: 8px;">여러가지 분석자료들 넣을 수 있으면 넣어보세요</div>
      </v-col>
    </v-row>

    <!-- Link Shortner 입력창 -->
    <v-row>
      <v-col cols="12">
        <LinkInput alert></LinkInput>
      </v-col>
    </v-row>

    <!-- 링크 -->
    <v-row>
      <v-col cols="12" v-for="link in linkList" :key="link._id">
        <v-card outlined hover>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="text-h6 text-truncate" style="color: #E71D36;">{{ link.Short_URL }}</v-list-item-title>
              <v-list-item-subtitle>{{ link.Make_Date }}</v-list-item-subtitle>
            </v-list-item-content>
            <v-spacer></v-spacer>
            <v-checkbox v-model="clickedLink" :value="link._id"></v-checkbox>
          </v-list-item>

          <v-card-subtitle class="py-0 font-weight-regular">브라우저탭에뜨는 이름</v-card-subtitle>
          <v-card-text class="text--primary pb-1">{{ link.Raw_URL }}</v-card-text>

          <v-card-actions class="px-4">
            <div><span class="info--text">#Empty</span></div>

            <v-spacer></v-spacer>

            <v-btn icon dark color="success" @click.stop="favoriteDialog = true;">
              <v-icon>mdi-heart-outline</v-icon>
            </v-btn>
            <v-btn icon dark color="info" @click.stop="tagDialog = true;">
              <v-icon>mdi-tag-outline</v-icon>
            </v-btn>
            <v-btn icon dark color="warning" @click.stop="hideDialog = true;">
              <v-icon>mdi-eye-off-outline</v-icon>
            </v-btn>
            <v-btn icon dark color="error" @click.stop="deleteDialog = true;">
              <v-icon>mdi-delete-outline</v-icon>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>

      <!-- 오류 -->
      <v-col cols="12" v-if="showError">
        <v-alert type="error">
          데이터 불러오기에 실패했습니다
        </v-alert>
      </v-col>

      <!-- 페이지네이션 -->
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
      <v-btn fab dark small color="error" :disabled="fabDisabled" @click.stop="deleteDialog = true;">
        <v-icon>mdi-delete</v-icon>
      </v-btn>
      <v-btn fab dark small color="warning" :disabled="fabDisabled" @click.stop="hideDialog = true;">
        <v-icon>mdi-eye-off</v-icon>
      </v-btn>
      <v-btn fab dark small color="info" :disabled="fabDisabled" @click.stop="tagDialog = true;">
        <v-icon>mdi-tag</v-icon>
      </v-btn>
      <v-btn fab dark small color="success" :disabled="fabDisabled" @click.stop="favoriteDialog = true;">
        <v-icon>mdi-heart</v-icon>
      </v-btn>
    </v-speed-dial>

    <!-- TODO: Dialog들 전부 components/Dialog로 옮기기 -->
    <v-dialog v-model="deleteDialog" max-width="360">
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
          <v-btn color="error" text class="font-weight-bold" @click="deleteDialog = false;">
            삭제
          </v-btn>
          <v-btn color="warning" text class="font-weight-bold" @click="deleteDialog = false;">
            취소
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- 숨김 Dialog -->
    <v-dialog v-model="hideDialog" max-width="360">
      <v-card>
        <v-card-title class="headline">
          링크 숨기기
        </v-card-title>
        <v-card-text class="pb-0">
          숨길 위치를 선택하세요<br/>
          선택 Menu나오기
        </v-card-text>
        <v-card-actions>
          <v-btn color="info" text class="font-weight-bold" @click="hideDialog = false;">
            위치 추가
          </v-btn>
          <v-spacer></v-spacer>
          <v-btn color="success" text class="font-weight-bold" @click="hideDialog = false;">
            숨기기
          </v-btn>
          <v-btn color="error" text class="font-weight-bold" @click="hideDialog = false;">
            취소
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- 태그추가 Dialog -->
    <v-dialog v-model="tagDialog" max-width="360">
      <v-card>
        <v-card-title class="headline">
          태그
          <v-spacer></v-spacer>
          <v-btn color="error" icon class="font-weight-bold" @click="tagDialog = false;">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-card-title>
        <v-card-text class="pb-0">
          <v-row>
            <v-col cols="6">
              <v-btn color="success" dark class="full-width" @click="tagChangeDialog = true;">
                태그 변경
              </v-btn>
            </v-col>
            <v-col cols="6">
              <v-btn color="error" dark class="full-width" @click="tagDeleteDialog = true;">
                태그 삭제
              </v-btn>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
    </v-dialog>

    <!-- 태그 변경 Dialog -->
    <v-dialog v-model="tagChangeDialog" max-width="360">
      <v-card>
        <v-card-title class="headline">태그 변경</v-card-title>
        <v-card-text class="pb-0">
          <v-text-field label="#태그" v-model="tagName"></v-text-field>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="success" text class="font-weight-bold" @click="tagChangeDialog = false;">
            변경
          </v-btn>
          <v-btn color="error" text class="font-weight-bold" @click="tagChangeDialog = false;">
            취소
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- 태그 삭제 Dialog -->
    <v-dialog v-model="tagDeleteDialog" max-width="320">
      <v-card class="py-2">
        <v-card-text class="pb-0">
          <v-container class="pb-0 text-subtitle-1 font-weight-medium black--text">
            해당 작업은 되돌릴 수 없습니다.<br/>
            태그를 지우시겠습니까?
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="success" text class="font-weight-bold" @click="tagDeleteDialog = false;">
            확인
          </v-btn>
          <v-btn color="error" text class="font-weight-bold" @click="tagDeleteDialog = false;">
            취소
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- 즐겨찾기 Dialog -->
    <v-dialog v-model="favoriteDialog" width="360">
      <v-card>
        <v-card-title class="headline">즐겨찾기 추가</v-card-title>
        <v-card-text>
          ~~~~~~~~~~ 을 즐겨찾기에 추가하시겠습니까?
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="success" text class="font-weight-bold" @click="favoriteDialog = false;">
            확인
          </v-btn>
          <v-btn color="error" text class="font-weight-bold" @click="favoriteDialog = false;">
            취소
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { mapState } from 'vuex'
import axios from 'axios'
import ShortenLink from '@/components/ShortenLink.vue'

export default {
  name: 'ManageHome',
  components: {
    LinkInput: ShortenLink
  },
  data: () => ({
    loading: false, // 로딩상태
    maxPage: 1, // 최대 페이지 번호
    page: 1, // 현재 페이지 번호
    itemPerPage: 10, // 페이지 당 아이템 갯수
    fab: false, // Floating Button 클릭 상태
    linkList: [], // 나의 링크 배열
    clickedLink: [], // 현재 클릭한 링크 아이디 배열
    tagName: '', // 변경할 태그 이름
    deleteDialog: false, // 삭제 dialog
    hideDialog: false, // 숨김 dialog
    tagDialog: false, // 태그 dialog
    tagChangeDialog: false, // 태그 변경 dialog
    tagDeleteDialog: false, // 태그 삭제 dialog
    favoriteDialog: false, // 즐겨찾기 dialog
    showError: false // 에러 표시
  }),
  created: function() {
    // 생성되었을 때 데이터 가져오기
    this.pageEnter()
  },
  watch: {
    // 라우트 변경시 데이터 가져오기 다시 호출
    '$route': 'pageEnter',
    // 페이지 변경시 다음 페이지 데이터 가져오기
    page: function(newPage) {
      this.startLoading()
      this.resetForPaging()
      this.page = newPage
      this.fetchLinkData(this.fetchError)
      this.stopLoading()
    }
  },
  computed: {
    ...mapState(['serverURL', 'userInfo']),
    fabDisabled: function() {
      return this.clickedLink.length === 0
    }
  },
  methods: {
    resetForPaging() {
      this.fab = false
      this.linkList.length = 0
      this.clickedLink.length = 0
      this.tagName = ''
      this.deleteDialog = false
      this.hideDialog = false
      this.tagDialog = false
      this.tagChangeDialog = false
      this.tagDeleteDialog = false
      this.favoriteDialog = false,
      this.showError = false
    },
    startLoading() {
      this.loading = true
    },
    stopLoading() {
      setTimeout(() => {this.loading = false}, 450)
    },
    pageEnter() {
      // 페이지에 들어올때마다 호출된다
      this.resetForPaging()
      this.startLoading()
      this.fetchLinkData(this.fetchError)
      this.stopLoading()
    },
    fetchError(e) {
      console.log(e)
      this.showError = true
    },
    fetchLinkData(errorFunc) {
      // 자신의 아이디에 해당하는 LinkList를 서버에서 가져온다
      axios.post(this.serverURL.linkPageURL,
        { user_id: this.userInfo.email, page: this.page, item_count: this.itemPerPage })
        .then(res => {
          this.maxPage = res.data.maxPage
          this.page = res.data.page
          this.linkList = res.data.list
        }).catch(e => {
          errorFunc(e)
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