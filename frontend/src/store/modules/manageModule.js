const RequestMode = Object.freeze({
  Single: Symbol("Single"),
  Multiple: Symbol("Multiple")
})

export default module = {
  // namespace가 존재하므로 사용할때는 {등록시킬때이름/}를 추가해줘서 사용해야 한다
  namespaced: true,
  state: () => ({
    RequestMode,
    showDrawer: true,  // Manage 페이지의 NavigationDrawer 상태값
    showError: false, // 에러 표시
    errorMsg: '', // 에러 메시지
    loading: false, // 로딩상태
    requestMode: RequestMode.Single,  // Request 요청시의 단독/여러개 상태값
    clickedLinkID: '', // 현재 클릭한 링크 아이디
    checkedLinkIDList: [] // 체크박스 체크한 링크 아이디 배열
  }),
  mutations: {
    setDrawer(state, value) {
      state.showDrawer = value
    },
    setError(state, value) {
      state.showError = value
    },
    setErrorMsg(state, value) {
      state.errorMsg = value
    },
    setLoading(state, value) {
      state.loading = value
    },
    setRequestMode(state, value) {
      switch (value) {
      case RequestMode.Single:
        state.requestMode = RequestMode.Single
        break
      default:
        state.requestMode = RequestMode.Multiple
        break
      }
    },
    setClickedLinkID(state, value) {
      state.clickedLinkID = value
    },
    setCheckedLinkIDList(state, value) {
      state.checkedLinkIDList = value
    }
  },
  actions: {
    toggleDrawer({state, commit}) {
      commit('setDrawer', (state.showDrawer ? false : true))
    },
    openDrawer({commit}) {
      commit('setDrawer', true)
    },
    closeDrawer({commit}) {
      commit('setDrawer', false)
    },
    showError({state, commit}, payload = '에러가 발생했습니다') {
      commit('setError', true)
      commit('setErrorMsg', payload)
    },
    hideError({commit}) {
      commit('setError', false)
    },
    startLoading({commit}) {
      commit('setLoading', true);
    },
    stopLoading({commit}) {
      commit('setLoading', false);
    },
    delayedStopLoading({commit}, payload = 450) {
      setTimeout(() => { commit('setLoading', false) }, 450)
    },
    clearSelectLink({state, commit}) {
      commit('setRequestMode', state.RequestMode.Single)
      commit('setClickedLinkID', '')
      commit('setCheckedLinkIDList', [])
    },
    changeClickedLinkID({commit}, payload) {
      commit('setClickedLinkID', payload)
    },
    changeCheckedLinkIDList({commit}, payload) {
      commit('setCheckedLinkIDList', payload)
    },
    changeRequestMode({commit}, payload) {
      commit('setRequestMode', payload)
    }
  },
  getters: {
    /* 전역적으로 모듈들이 동일한 포맷의 mutations를 사용할 때 이곳에 등록해서 사용한다 */
    linkID: (state) => {
      switch (state.requestMode) {
      case state.RequestMode.Single:
        return [state.clickedLinkID]
      default:
        return state.checkedLinkIDList
      }
    }
  }
}

