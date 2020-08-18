const main = {
  namespaced: true,
  state: {
    mainLinks: [
      {name: 'Main', href: '#'},
      {name: 'About', href: '#about'},
      {name: 'Contact', href: '#contact'}
    ],
    drawer: false,
    tabIndex: 0
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
    }
  }
}

export default main