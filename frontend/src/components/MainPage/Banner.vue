<template>
  <v-img :src="imgPath" :height="height" dark>
    <v-row class="fill-height overlay" align="center">
      <v-col>
        <blockquote>
          <p>
            <span data-duration="1.1" data-delay=".23">"The&nbsp;</span>
            <span data-duration="1.1" data-delay=".43">Simpler&nbsp;</span>
            <span data-duration="1.8" data-delay=".42">It&nbsp;</span>
            <span data-duration="1.2" data-delay=".25">Is,&nbsp;</span>
            <span data-duration="1.7" data-delay=".30">The&nbsp;</span>
            <span data-duration="1.2" data-delay=".29">Better&nbsp;</span>
            <span data-duration="1.4" data-delay=".26">I&nbsp;</span>
            <span data-duration="1.7" data-delay=".19">Like&nbsp;</span>
            <span data-duration="1.2" data-delay=".11">It."&nbsp;</span>
          </p>
          <cite>Peter Lynch</cite>
        </blockquote>
      </v-col>
    </v-row>
  </v-img>
</template>

<script>
export default {
  name: 'Banner',
  data: () => ({
    imgPath: require('@/assets/img/Banner_005.jpg')
  }),
  methods: {
    setTextAnimation() {
      const words = this.$el.getElementsByTagName('span')
      const cite = this.$el.getElementsByTagName('cite')[0]
      let maxDelay = 0, maxDuration = 0                   // 애니메이션 주기

      // 각 단어에 개별 애니메이션을 추가한다.
      for (let i=0; i < words.length; i++) {
        const word = words[i]
        const duration = word.dataset.duration
        const delay = word.dataset.delay
        const blur = word.dataset.blur
        
        maxDelay = Math.max(delay, maxDelay)
        maxDuration = Math.max(duration, maxDuration)

        word.style.transition = `all ${duration}s ease-in ${delay}s`
        word.classList.add('animate')
      }

      // cite(인물명)은 가장 마지막에 떠오른다.
      cite.style.transition = `all ${maxDuration}s ease-in ${maxDelay}s`
      cite.classList.add('animate')

      // 모든 글자가 떠오른 후 다시 없앤다.
      const maxTransition = (maxDuration + maxDelay) * 1000
      setTimeout(() => {
        const baseDelay = 5000; // 5초동안 표시

        // baseDelay만큼 표시한 후 글자를 없앤다.
        setTimeout(() => {
          words.forEach(function(word) {
            word.classList.remove('animate')
          })
          cite.classList.remove('animate')
        }, baseDelay)

        // 이후 재귀적으로 무한반복
        setTimeout(() => {
          this.setTextAnimation()
        }, baseDelay + maxTransition*2)
      }, maxTransition)
    }
  },
  mounted() {
    this.setTextAnimation()
  },
  props: {
    type: {
      type: String,
      default: 'page'
    },
    height: {
      type: String,
      default: "200"
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Recursive:wght@300;400;500&display=swap');

.overlay {
  background: rgba(0,0,0,0.26)
}
p {
  font-family: 'Recursive', sans-serif;
  font-size: 2.6rem;
  font-style: italic;
}
span {
  opacity: 0;
}
span.animate {
  opacity: 1;
}
cite {
  font-style: normal;
  opacity: 0;
}
cite.animate {
  opacity: 1;
}
</style>