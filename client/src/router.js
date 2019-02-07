import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

import notFound from '@/components/notFound'

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/components/Home.vue')
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('@/components/About.vue')
    },
    {
      path: '/fix',
      name: 'fix',
      component: () => import('@/components/Fix.vue')
    },
    {
      path: '*',
      name: 'notfound',
      component: notFound
    }
  ]
})
