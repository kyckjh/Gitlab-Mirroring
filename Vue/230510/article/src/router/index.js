import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CreateView from '@/views/CreateView'
import DetailView from '@/views/DetailView'
import NotFound404 from '@/views/NotFound404'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
  {
    path: '/articles/:articleId',
    name: 'detail',
    component: DetailView
  },
  {
    path: '/404',
    name: 'notfound404',
    component: NotFound404
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
