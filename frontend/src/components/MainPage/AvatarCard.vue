<template>
  <v-card 
    class="mx-5 my-8" 
    :min-height="minHeight" 
    :min-width="minWidth"
    :max-width="maxWidth"
    :style="[cardStyle, mouseHover ? hoverStyle : '']"
    @mouseenter="mouseHover = true"
    @mouseleave="mouseHover = false"
    >
    <!-- 상단 중앙 아바타 -->
    <div class="text-center" :style="{height: `${iconDivHeight}px`}">
      <v-avatar class="mx-auto" :style="iconStyle" :size="iconSize" color="white" rounded>
        <v-icon :size="iconSize * (3/5)" color="rgb(55,115,165)">{{icon}}</v-icon>
      </v-avatar>
    </div>
    <!-- 카드 타이틀 -->
    <v-card-title class="justify-center title pt-1" :style="titleStyle">
      <slot name="title" />
    </v-card-title>
    <!-- 카드 내용 -->
    <v-card-text class="px-8" :class="textContent">
      <slot name="content" />
    </v-card-text>
    <!-- 카드 하단 버튼 영역-->
    <v-card-actions class="px-8">
      <slot name="actions" />
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'AvatarCard',
  data: () => ({
    mouseHover: false,
  }),
  props: {
    icon: String,
    iconSize: {
      type: Number,
      default: () => 100
    },
    iconHoist: {
      type: Boolean,
      default: () => false
    },
    titleSize: {
      type: Number,
      default: () => 1.5
    },
    borderWidth: {
      type: Number,
      default: () => 2
    },
    borderColor: {
      type: String,
      default: () => 'rgb(55,115,165)'
    },
    hoverWidth: {
      type: Number,
      default: () => 3
    },
    hoverColor: {
      type: String,
      default: () => 'rgb(55,115,165)'
    },
    minWidth: {
      type: String,
      default: () => '250px'
    },
    minHeight: {
      type: String,
      default: () => '300px'
    },
    maxWidth: {
      type: String,
      default: () => '360px'
    },
    textContent: {
      type: String,
      default: () => 'text-justify'
    }
  },
  computed: {
    iconStyle() {
      return {
        position: 'relative',
        top: `-${this.iconHoist ? this.iconSize/2 : 0}px`,
        'border-radius': '50% !important'
      }
    },
    iconDivHeight() {
      return this.iconHoist ? this.iconSize/2 : this.iconSize
    },
    titleStyle() {
      return {
        fontSize: `${this.titleSize}em !important`
      }
    },
    cardStyle() {
      return {
        border: `${this.borderWidth}px solid ${this.borderColor}`,
        transition: 'transform .2s'
      }
    },
    hoverStyle() {
      return {
        border: `${this.hoverWidth}px solid ${this.hoverColor}`,
        transform: 'scale(1.1)'
      }
    }
  }
}
</script>

<style scoped>
</style>