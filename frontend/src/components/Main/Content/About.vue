<template>
  <div class="mb-9 mt-12" id="about">
    <SubHeader title="About">
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

            <template v-slot:content>
              Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nulla odio autem ducimus libero odit, nisi rem ipsam omnis porro veritatis unde suscipit in reprehenderit eveniet sapiente molestias natus incidunt laudantium?
            </template>
          </AvatarCard>
        </v-col>
        <v-col cols="12" sm="9" md="4">
          <AvatarCard icon="share">
            <template v-slot:title>
              Share
            </template>

            <template v-slot:content>
              Lorem ipsum dolor sit, amet consectetur adipisicing elit. Harum iusto ipsam reiciendis, eum quo ea, veritatis, culpa debitis dolorum perspiciatis voluptate ab dignissimos eius? Exercitationem, soluta! Iste officia iure exercitationem!
            </template>
          </AvatarCard>
        </v-col>
        <v-col cols="12" sm="9" md="4">
          <AvatarCard icon="poll">
            <template v-slot:title>
              Manage
            </template>

            <template v-slot:content>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Iste incidunt, reiciendis eaque harum deleniti, necessitatibus fuga repellat beatae dolorum voluptas sequi, ipsam sint perspiciatis delectus maxime libero consequatur! Unde, aspernatur!
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
  name: 'About',
  components: {
    SubHeader, AvatarCard
  }
}
</script>

<style>

</style>