<template>
  <div class="my-9" id="about">
    <SubHeader title="Features">
      MiniPy provides simplified version of any links ready to share on SNSs, blogs and everywhere. <br>
      Just with one click, create, manage, share altogether come in handy. <br>
    </SubHeader>

    <v-container class="limit-width mt-5">
      <v-row justify="center">
        <v-col cols="7" md="4">
          <AvatarCard />
        </v-col>
        <v-col cols="7" md="4">
          <AvatarCard />
        </v-col>
        <v-col cols="7" md="4">
          <AvatarCard />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import SubHeader from './SubHeader.vue'
import AvatarCard from './AvatarCard.vue'
export default {
  name: 'Features',
  components: {
    SubHeader, AvatarCard
  }
}
</script>

<style>

</style>