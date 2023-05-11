import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HelloView from '@/views/HelloView'
import AboutView from '@/views/AboutView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView  
  },
  {
    path:'/about',
    name:'about',
    component: AboutView,
    beforeEnter(to, from, next){
      next({name:'hello', params:{userName:'About'}})
    }
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})
router.beforeEach((to, from, next)=> {
  // console.log('이거 실행됩니다.')
  // console.log(to)
  // console.log(from)
  // if(to.name != 'about'){
  //   next({name:'about'})
  // } else {
  //   next()
  // }
  next()
})


export default router
