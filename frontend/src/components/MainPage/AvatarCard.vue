<template>
  <v-card class="mx-5 my-8" min-height="300px" max-width="360px">
    <div class="text-center" :style="{height: `${iconSize/2}px`}">
      <!-- 상단 중앙 아바타 -->
      <v-avatar class="mx-auto" :style="styles" :size="iconSize" color="white" rounded>
        <v-icon size="60" color="rgb(55,115,165)">{{icon}}</v-icon>
      </v-avatar>
    </div>
    <!-- 카드 타이틀 -->
    <v-card-title class="justify-center title pt-1">
      <slot name="title" />
    </v-card-title>
    <v-card-text class="px-8 text-justify">
      <slot name="content" />
    </v-card-text>
    <v-card-actions class="px-8">
      <slot name="actions" />
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: 'AvatarCard',
  props: {
    icon: String,
    iconSize: {
      type: Number,
      default: 100
    }
  },
  computed: {
    styles() {
      return {
        position: 'relative',
        top: `-${this.iconSize/2}px`,
        'border-radius': '50% !important'
      }
    }
  }
}
</script>

<style scoped>
.v-card__title {
  font-size: 1.5em !important;
}
.v-card {
  border: 2px solid rgb(55,115,165);
}
</style>