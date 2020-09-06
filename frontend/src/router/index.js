import Vue from 'vue'
import store from '@/store/index.js'
import VueRouter from 'vue-router'
import MainPage from '@/views/MainPage.vue'
import AppDrawer from '@/views/MainPage/AppDrawer.vue'
import AppFooter from '@/views/MainPage/AppFooter.vue'
import AppNavBar from '@/views/MainPage/AppNavBar.vue'
import ManagePage from '@/views/ManagePage.vue'
import ManageNavBar from '@/views/ManagePage/ManageNavBar.vue'
import ManageNavDrawer from '@/views/ManagePage/ManageDrawer.vue'
import {userLogout} from '@/assets/js/account.js'

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
        component: () => import(/* webpackChunkName: "main" */ '@/views/MainPage/MainHome.vue'),
      },
      {
        path: 'api',
        name: 'MainAPI',
        component: () => import(/* webpackChunkName: "main" */ '@/views/MainPage/MainAPI.vue'),
      }
    ],
  },
  {
    path: '/manage',
    components: {
      default: ManagePage,
      navBar: ManageNavBar,
      drawer: ManageNavDrawer
    },
    children: [
      {
        path: '',
        name: 'ManageHome',
        component: () => import(/* webpackChunkName: "manageHome" */ '@/views/ManagePage/ManageHome.vue')
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

router.beforeEach(function(to, from, next) {
  const loggedIn = store.state.userInfo.loggedIn
  const expiresAt = store.state.userInfo.expiresAt

  // 로그인 기간이 만료된 경우 자동 로그아웃
  if (expiresAt) {
    const now = new Date().getTime()

    if (now >= expiresAt) {
      userLogout()
      next({name: 'Main'})
    }
  }

  // 홈페이지인 경우
  if (to.matched.some(record => record.name === 'Home')) {
    //로그인된 유저는 Manage로, 아니면 Main으로 돌린다.
    if (loggedIn) next({name: 'ManageHome'})
    else next({name: 'Main'})
  // Main 페이지 계열인 경우
  } else if (to.matched.some(record => record.name === 'Main')) {
    // 로그인된 유저는 Manage로, 아니면 그대로 진행한다.
    if (loggedIn) next({name: 'ManageHome'})
    else next()
  // Manage 페이지 계열인 경우
  } else if (to.matched.some(record => record.name === "Manage")) {
    // 비로그인 유저는 Main으로, 아니면 그대로 진행한다.
    if (!loggedIn) {
      alert("로그인이 필요한 서비스입니다.")
      next({name: 'MainHome'})
    } else next()
  // 이외의 경우 그대로 진행
  } else {
    next()
  }
})

export default router
