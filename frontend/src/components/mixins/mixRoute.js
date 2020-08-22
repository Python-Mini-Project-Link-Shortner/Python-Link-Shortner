import {mapMutations} from 'vuex'

const mixRoute = {
  methods: {
    ...mapMutations(['setIntersection']),
    // 스크롤인지 라우터인지 확인한다.
    scrollOrRoute(href) {
      // #이 포함되어 있는 경우는 스크롤
      if (href.includes('#')) return 'scroll'
      else return 'route'
    },
    goTo(item) {
      const duration = 1000
      const href = item.href
      const behavior = this.scrollOrRoute(href)

      // scroll로 동작할 경우
      if (behavior === 'scroll') {
        // 스크롤 실행 동안 Intersection 비활성화
        this.setIntersection(false)
        setTimeout(() => {
          this.setIntersection(true)
        }, duration)
    
        // 스크롤 이동
        this.$vuetify.goTo( 
          href === "#" ? 0 : href, { duration: duration }
        )
      // route로 동작할 경우
      } else if (behavior === 'route') {
        const router = this.$router

        router.push(item.href)
      }
    }
  }
}

export default mixRoute