import {createApp} from 'vue'; 
import Header from './Header.vue'
import PackageApp from './PackageApp.vue'
import VueAxios from 'vue-axios'
import axios from 'axios'
import Admin from './Admin.vue'

createApp(Header).mount("#header")
createApp(PackageApp).use(VueAxios,axios).mount("#packagelist")
createApp(Admin).use(VueAxios,axios).mount("#admin")



