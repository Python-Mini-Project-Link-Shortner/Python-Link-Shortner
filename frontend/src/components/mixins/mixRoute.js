import {mapMutations} from 'vuex'

const mixRoute = {
  methods: {
    ...mapMutations(['setIntersection']),
    // 스크롤인지 라우터인지 확인한다.
    scrollOrRoute(href) {
      const currentURL = window.location.href
      const currentOrigin = window.location.origin + '/#'
      // Path: 전체경로에서 origin과 뒤에 붙은 '/'을 제거한다.
      const currentPath = (currentURL[currentURL.length - 1] === '/') ?
        currentURL.replace(currentOrigin, '').slice(0, -1) : currentURL.replace(currentOrigin, '')
      
      // #이 포함되어 있는 경우
      if (href.includes('#')) {
        const targetPath = href.slice(0, href.indexOf('#'))
        const targetAnchor = href.slice(href.indexOf('#'))

        // 페이지가 변하지 않는 경우는 스크롤
        if (currentPath === targetPath) 
          return {type: 'scroll', anchor: targetAnchor}
        // 페이지가 변하는 경우 라우트
        else 
          return {type: 'route', path: targetPath, anchor: targetAnchor}

      // #이 없으면 라우트
      } else return {type: 'route', path: href, anchor: ''}
    },
    goTo(item) {
      const duration = 1000
      const behavior = this.scrollOrRoute(item.href)
      
      // scroll로 동작할 경우
      if (behavior.type === 'scroll') {
        // 스크롤 실행 동안 Intersection 비활성화
        this.setIntersection(false)
        setTimeout(() => {
          this.setIntersection(true)
        }, duration)
    
        // 스크롤 이동
        this.$vuetify.goTo( 
          behavior.anchor === "#" ? 0 : behavior.anchor, { duration: duration }
        )
      // route로 동작할 경우
      } else if (behavior.type === 'route') {
        const router = this.$router
        
        router.push(behavior.path)
        
        // 스크롤까지 해야하는 경우
        if (behavior.anchor) {
          // DOM 로딩 이후 스크롤한다.
          this.$nextTick(() => {
            this.goTo(item)
          })
        }
      }
    }

  }
}

export default mixRoute