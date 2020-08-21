const main = {
  namespaced: true,
  state: {
    mainLinks: [
      {name: 'Main', href: '#'},
      {name: 'About', href: '#about'},
      {name: 'Contact', href: '#contact'},
      {name: 'API', href: '/api'}
    ],
    intersectEnabled: true,
    drawer: false,
    tabIndex: 0,
    listIndex: 0
  },
  mutations: {
    toggleDrawer(state) {
      state.drawer = !state.drawer
    },
    setDrawer(state, payload) {
      state.drawer = payload
    },
    setTabIndex(state, payload) {
      payload = Number(payload)
      state.tabIndex = payload
    },
    setListIndex(state, payload) {
      payload = Number(payload)
      state.listIndex = payload
    },
    setIntersection(state, payload) {
      state.intersectEnabled = payload
    }
  }
}

export default main