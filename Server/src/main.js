import {createApp} from 'vue'; 
import Header from './Header.vue'
import PackageApp from './PackageApp.vue'
import VueAxios from 'vue-axios'
import axios from 'axios'
createApp(Header).mount("#header")
const app = createApp(PackageApp)

app.use(VueAxios,axios).mount("#packagelist")





