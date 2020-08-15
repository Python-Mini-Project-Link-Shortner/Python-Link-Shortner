<template>
    <v-footer color="rgb(67,66,66)">
        <v-container class="white--text" style="max-width: 1200px">
            <v-row>
                <v-col class="text-center" cols="12">
                    <Logo />
                </v-col>
                <v-col class="text-center overline grey--text font-weight-light pa-0" cols="12">
                    © {{new Date().getFullYear() }} MiniPy. All rights reserved.
                </v-col>
            </v-row>
        </v-container>
    </v-footer>
</template>

<script>
import Logo from './Content/Logo.vue'

export default {
    name: 'AppFooter',
    components: {
        Logo
    }
}
</script>

<style>

</style>