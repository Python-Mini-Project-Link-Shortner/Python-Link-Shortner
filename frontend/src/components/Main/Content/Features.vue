<template>
  <div class="mb-9 mt-12" id="about">
    <SubHeader title="Features">
      MiniPy provides simplified version of any links ready to share on SNSs, blogs, Etc. <br>
      Just with one click— shorten, share, manage altogether come in handy. <br>
    </SubHeader>

    <v-container class="limit-width mt-5">
      <v-row justify="center">
        <v-col cols="12" sm="9" md="4">
          <AvatarCard icon="fa-link">
            <template v-slot:title>
              Shorten
            </template>
          </AvatarCard>
        </v-col>
        <v-col cols="12" sm="9" md="4">
          <AvatarCard icon="share">
            <template v-slot:title>
              Share
            </template>
          </AvatarCard>
        </v-col>
        <v-col cols="12" sm="9" md="4">
          <AvatarCard icon="poll">
            <template v-slot:title>
              Manage
            </template>
          </AvatarCard>
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