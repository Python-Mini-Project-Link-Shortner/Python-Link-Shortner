import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from '@/views/MainPage.vue'
import AppDrawer from '@/views/MainPage/AppDrawer.vue'
import AppFooter from '@/views/MainPage/AppFooter.vue'
import AppNavBar from '@/views/MainPage/AppNavBar.vue'
import ManageNavBar from '@/views/ManagePage/ManageNavBar.vue'
import ManageNavDrawer from '@/views/ManagePage/ManageDrawer.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    redirect: {name: 'Main'}
  },
  {
    path: '/main',
    components:  {
      default: MainPage,
      navBar: AppNavBar,
      drawer: AppDrawer,
      footer: AppFooter
    },
    children: [
      {
        path: '',
        name: 'Main',
        component: () => import(/* webpackChunkName: "main" */ '@/views/MainPage/MainHome.vue')
      },
      {
        path: 'api',
        name: 'MainAPI',
        component: () => import(/* webpackChunkName: "main" */ '@/views/MainPage/MainAPI.vue')
      }
    ]
  },
  {
    path: '/manage',
    name: 'Manage',
    components: {
      default: () => import(/* webpackChunkName: "manage" */ '@/views/Manage.vue'),
      navBar: ManageNavBar,
      drawer: ManageNavDrawer
    }
  }
  // {
  //   path: '/about',
  //   name: 'About',
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // }
]

const router = new VueRouter({
  routes
})

export default router
