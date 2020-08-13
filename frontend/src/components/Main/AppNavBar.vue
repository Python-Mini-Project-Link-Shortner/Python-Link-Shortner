<template>
    <v-app-bar app color="white">
        <v-container class="limit-width" fluid>
            <v-row align="center">
                <v-app-bar-nav-icon
                  class="hidden-md-and-up"
                  @click="drawer = !drawer"
                />
                <!-- MiniPy 타이틀 표시하는 부분 -->
                <v-toolbar-title>
                    <router-link tag="a" :to="{name: 'Main'}" class="logo no-drag">
                        &lt; Mini<span class="py">Py</span> &gt;
                    </router-link>
                </v-toolbar-title>

                <v-spacer />

                <div>
                    <v-tabs
                     class="hidden-sm-and-down" 
                     background-color="transparent"
                     slider-size="2"
                     >
                        <v-tab 
                          v-for="item in menuItems" 
                          :key="item.name" 
                          :ripple="false"
                        >
                            {{item.name}}
                        </v-tab>
                    </v-tabs>
                </div>

                <v-btn color="rgb(55,115,165)" dark class="mx-3">Login</v-btn>
            </v-row>
        </v-container>
    </v-app-bar>
</template>

<script>
export default {
    name: 'AppNavBar',
    data: () => ({
        menuItems: [
            {name: 'Main', href: ''},
            {name: 'About', href: ''},
            {name: 'Contact', href: ''}
        ],
        drawer: false
    })
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
.limit-width {
    max-width: 1200px;
}
</style>