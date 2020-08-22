import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    redirect: {name: 'Main'}
  },
  {
    path: '/main',
    component: () => import(/* webpackChunkName: "main" */ '@/views/MainPage.vue'),
    children: [
      {
        path: '',
        name: 'Main',
        component: () => import(/* webpackChunkName: "main" */ '@/views/MainPage/MainHome.vue')
      },
      {
        path: 'api',
        name: 'MainAPI',
        component: () => import(/* webpackChunkName: "api" */ '@/views/MainPage/MainAPI.vue')
      }
    ]
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
