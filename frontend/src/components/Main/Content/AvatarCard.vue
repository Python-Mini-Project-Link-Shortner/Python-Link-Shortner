<template>
  <v-card class="mx-3 my-5" >
    <v-row justify="center">
      <v-avatar class="mx-auto" size="80" color="white" rounded>
        <v-icon size="64" color="rgb(55,115,165)">fa-link</v-icon>
      </v-avatar>
    </v-row>
    <v-card-text>
      asd
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'AvatarCard',
  props: {
    icon: String
  }
}
</script>

<style scoped>
.v-avatar {
  position: relative;
  top: -40px;
  border-radius: 50% !important;
}
.v-card {
  border: 2px solid rgb(55,115,165);
}
</style>