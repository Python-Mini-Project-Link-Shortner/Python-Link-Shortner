<template>
  <!--
    검색바
    @property {flat} solo나 solo-inverted일 때 그림자 비활성화
    @property {solo} focus 되기 전까지 투명한 상태로 활성화
    @property {hide-details} 메뉴 위에 있어서 hint가 추가되면 레이아웃 깨지므로 가려준다
    @property {dense} 높이 최적화
    @property {outlined} 외곽선 형태로 변경
    @property {label} 아무 입력도 없을 때 나오는 단어
  -->
  <v-text-field flat solo hide-details dense outlined
  label="검색" v-model="searchText" class="mr-2" @keyup.enter="search()">
    <v-icon slot="append" :color="this.searchText === '' ? 'error' : 'success'" @click="search()">
        mdi-text-box-search
      </v-icon>
  </v-text-field>
</template>

<script>
export default {
  name: 'SearchBar',
  data: () => ({
    searchText: '' // 검색 텍스트
  }),
  methods: {
    search() {
      if (this.searchText === '') {
        alert("한 글자 이상 입력해주세요");
      }
    }
  }
}
</script>

<style>

</style>