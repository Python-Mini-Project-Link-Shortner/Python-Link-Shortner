import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const routes = [
{
  path: '/',
  name: 'Home',
  component: Home
},
{
  path: '/about',
  name: 'About',
  // route level code-splitting
  // this generates a separate chunk (about.[hash].js) for this route
  // which is lazy-loaded when the route is visited.
  component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
},
{
  path: '/manage',
  name: 'Manage',
  component: () => import(/* webpackChunkName: "manage" */ '@/views/Manage.vue')
  // children: [ { path: '...', component: ... }, ...] 로 자식 만들기
}]

const router = new VueRouter({
  routes
})

export default router
