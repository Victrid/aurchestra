import {createApp} from 'vue'; 
import Header from './Header.vue'
import PackageApp from './PackageApp.vue'
import VueAxios from 'vue-axios'
import axios from 'axios'
import Admin from './Admin.vue'
import Home from './Home.vue'
import { createStore } from 'vuex'
import createPersistedState from "vuex-persistedstate";
const store = createStore({
    state:{
        username:'',
        password:''
    },
    mutations:{
        cacheUserInfo(state,username,password){
            state.username=username;
            state.password=password
        }
    },
    plugins: [createPersistedState({
        storage: window.sessionStorage,
    })],
})

createApp(Header).mount("#header")
createApp(PackageApp).use(VueAxios,axios).mount("#packagelist")
createApp(Admin).use(VueAxios,axios).use(store).mount("#admin")
createApp(Home).mount("#home-content")



