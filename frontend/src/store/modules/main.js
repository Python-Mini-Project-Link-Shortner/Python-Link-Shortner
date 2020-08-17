const main = {
	namespaced: true,
	state: () => ({
		mainLinks: [
			{name: 'Main', href: '#'},
			{name: 'About', href: '#about'},
			{name: 'Contact', href: '#contact'}
		],
		drawer: false,
	}),
	mutations: () => ({
		toggleDrawer(state) {
      state.drawer = !state.drawer
    },
    setDrawer(state, payload) {
      state.drawer = payload
    }
	})
}

export default main