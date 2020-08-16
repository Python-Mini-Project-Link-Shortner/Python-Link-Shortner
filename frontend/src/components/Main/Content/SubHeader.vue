<template>
    <div class="text-center">
        <h3 class="display-2">{{title}}</h3>
        <div class="decor mx-auto my-5">
            <v-divider class="decor primary"></v-divider>
        </div>
        <div class="mx-auto" style="max-width: 800px">
            <slot />
        </div>
    </div>
</template>

<script>
export default {
    name: 'SubHeader',
    props: ['title']
}
</script>

<style scoped>
    .decor {
        width: 50px;
    }
    .v-divider {
        border-width: 4px 0 0 0 !important;
    }
</style>