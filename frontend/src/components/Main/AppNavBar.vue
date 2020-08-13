<template>
    <v-container>
        <v-app-bar app>
            <v-toolbar-title>
                <router-link tag="a" :to="{name: 'Main'}" class="logo no-drag">
                    &lt; Mini<span class="py">Py</span> &gt;
                </router-link>
            </v-toolbar-title>

            <v-spacer />
            <div>
                <v-tabs class="hidden-sm-and-down" background-color="transparent">
                    <v-tab />
                </v-tabs>
            </div>
        </v-app-bar>
    </v-container>
</template>

<script>
export default {
    name: 'AppNavBar'
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Recursive:wght@300;400;500&display=swap');

.logo {
    font-family: 'Recursive', sans-serif;
    font-weight: 300;
    font-size: 2em;
    text-decoration: none;
    color: inherit;
}
.logo .py {
    color: rgb(55,115,165);
}
.no-drag {
    -ms-user-select: none; 
    -moz-user-select: -moz-none;
    -webkit-user-select: none; 
    -khtml-user-select: none; 
    user-select:none;
} 
</style>