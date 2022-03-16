import { createApp } from 'vue'
import App from './App.vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

//import vue-axios module
import VueAxios from 'vue-axios'
import axios from 'axios';



// Route
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

const app = createApp(App)
app.use(ElementPlus)
app.use(router)
app.use(VueAxios,axios)
app.mount('#app')
