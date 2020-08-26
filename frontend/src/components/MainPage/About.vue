<template>
  <div class="mb-9 mt-12" id="about">
    <SubHeader title="About">
      MiniPy provides simplified version of any links ready to share on SNSs, blogs, etc. <br>
      Just with one click— shorten, share, manage altogether come in handy. <br>
    </SubHeader>

    <v-container class="limit-width mt-5">
      <v-row justify="center">
        <v-col class="d-flex justify-center" cols="12" sm="9" md="4">
          <AvatarCard icon="fa-link">
            <template v-slot:title>
              Shorten
            </template>

            <template v-slot:content>
              Lenghy URLs that take up almost 3 or 4 lines long are just eyesores to everyone. They look unnatural and simply ruin your message. Copy your messy link and hit the shorten button. We will deliver you a nice and clean link.
            </template>
          </AvatarCard>
        </v-col>
        <v-col class="d-flex justify-center" cols="12" sm="9" md="4">
          <AvatarCard icon="share">
            <template v-slot:title>
              Share
            </template>

            <template v-slot:content>
              Many Social Networks have its limit on each post. Some messagings cost more if exceeded. A shortened link will not only solve these problems but enhance the readability of your message when shared.
            </template>
          </AvatarCard>
        </v-col>
        <v-col class="d-flex justify-center" cols="12" sm="9" md="4">
          <AvatarCard icon="poll">
            <template v-slot:title>
              Manage
            </template>

            <template v-slot:content>
              MiniPy provides analytical data that allow for making smarter decisions on your projects. You will see how many clicks your link gained, what browsers people prefer, from where they clicked, click-through rates on a daily basis, and whatnots.
            </template>

            <template v-slot:actions>
              <GLoginBtn class="mb-3" block long />
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
import GLoginBtn from '@/components/GLoginBtn.vue'

export default {
  name: 'About',
  components: {
    SubHeader, AvatarCard, GLoginBtn
  }
}
</script>

<style>

</style>