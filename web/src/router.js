import {createRouter, createWebHashHistory } from 'vue-router'
import HomePage from './components/HomePage.vue'
import Admin from './components/AdminLogin.vue'
import Arch from './components/ArchPackage.vue'

const routes = [
    {path: '/',component:HomePage},
    {path: '/admin',component:Admin},
    {path: '/arch',component:Arch}
]
const router = createRouter({
    history:createWebHashHistory(),
    routes: routes
})
export default router;