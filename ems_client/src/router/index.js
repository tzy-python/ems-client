import Vue from 'vue'
import Router from 'vue-router'
import Login from "../components/Login";
import Register from "../components/Register";
import Index from "../components/Index";
import Add_emp from "../components/Add_emp";
import Update from "../components/Update";



Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Login',
      component:Login,
    },
    {
      path: '/login',
      name: 'Login',
      component:Login,
     },
    {
      path: '/register',
      name: 'Register',
      component:Register,
    },
    {
      path: '/index',
      name: 'Index',
      component:Index,
    },
    {
      path: '/add',
      name: 'Add',
      component:Add_emp,
    },
    {
      path: '/update',
      name: 'Update',
      component:Update,
    },
    {
      path: '/update/:id',
      name: 'Update',
      component:Update,
    },
  ]
})
