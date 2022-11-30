import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
  {
  path: '/index',
  name: 'index',
  component: () => import('../views/index.vue')
},{
  path: '/index_demo',
  name: 'index_demo',
  component: () => import('../views/index_demo.vue')
},
{
  path: '/',
  name: 'Login',
  component: () => import('../views/Login.vue')
},
{
  path: '/register',
  name: 'Register',
  component: () => import('../views/register.vue')
},
{
  path: '/devicemanage',
  name: 'Devicemanage',
  component: () => import('../views/Devicemanage.vue')
},
{
  path: '/model',
  name: 'Model',
  component: () => import('../views/model.vue')
},
{
  path: '/datamanage',
  name: 'Datamanage',
  component: () => import('../views/Datamanage.vue')
},
{
  path: '/jobmanage',
  name: 'Jobmanage',
  component: () => import('../views/Jobmanage.vue')
},
{
  path: '/addjob',
  name: 'Addjob',
  component: () => import('../views/addjob.vue')
},
{
  path: '/model_analysis',
  name: 'Model_analysis',
  component: () => import('../views/model_analysis.vue')
},
{
  path: '/myjob',
  name: 'Myjob',
  component: () => import('../views/myjob.vue')
},



]
const router = new VueRouter({
  mode: "history",
  routes
})

export default router