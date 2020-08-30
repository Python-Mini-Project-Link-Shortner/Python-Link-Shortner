<template>
  <v-container class="text-left" px-6 py-5 fluid>
    <v-row>
      <v-col cols="12">
        <div style="height: 240px; background-color: cyan; border-radius: 8px;">여러가지 분석자료들 넣을 수 있으면 넣어보세요</div>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12">
        <LinkInput alert></LinkInput>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="12" class="text-right">
        <v-btn class="mx-2" color="primary" :disabled="favoriteDisable">관심등록</v-btn>
        <v-btn class="mx-2" color="error" :disabled="removeDisable">삭제</v-btn>
        <v-btn class="mx-2" color="success" :disabled="tagDisable">#태그</v-btn>
        <v-btn class="mx-2" color="secondary" :disabled="hideDisable">숨기기</v-btn>
      </v-col>

      <v-col cols="12" v-for="n in 10" :key="n">
        <v-card :elevation="3">
          <v-list-item class="grey lighten-2 height-48">
            <div class="text-truncate font-weight-bold">탭이름 (길면...)</div>
            <v-spacer></v-spacer>
            <div class="grey--text lighten-1 pr-4 ">2020-08-13</div>
            <v-checkbox v-model="checkboxTest[n - 1]"></v-checkbox>
          </v-list-item>
          <v-divider class="grey lighten-1"></v-divider>

          <v-card-text>
            <div class="text-h6 red--text text--darken-1 pb-1">pysh.com/ABC</div>
            <div class="text-truncate">http://naver.com</div>
          </v-card-text>

          <v-card-actions class="px-3 pt-0">
            <v-btn outlined color="primary">복사</v-btn>
            <v-btn outlined color="error">제거</v-btn>
            <v-btn outlined color="secondary">탭이름 변경</v-btn>
            <v-btn outlined color="success">#태그</v-btn>
            <v-btn outlined color="warning">기타</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>

      <v-col cols="12">
        <v-pagination v-model="page" prev-icon="mdi-menu-left" next-icon="mdi-menu-right" :length="10" :total-visible="10"></v-pagination>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ShortenLink from '@/components/ShortenLink.vue'

export default {
  name: 'Manage',
  components: {
    LinkInput: ShortenLink
  },
  data: () => ({
    page: 1,
    favoriteDisable: true,
    removeDisable: true,
    tagDisable: true,
    hideDisable: true,
    checkboxTest: []
  }),
  methods: {
  }
}
</script>

<style scoped>
  .height-48 {
    height: 48px !important;
  }
</style>