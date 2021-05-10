import { createApp } from 'vue'
import App from './App.vue'
// eslint-disable-next-line
import $ from 'jquery'
import "bootstrap";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";
import axios from "axios";
import 'animate.css';
import {router} from "@/router";

axios.get('./config.json').then((result)=>{
    localStorage.setItem('ApiUrl',result.data.ApiUrl);
}).catch((error)=>{console.log(error)})
router.beforeEach((to,from,next)=>{
    if(to.meta.title){
        document.title=to.meta.title
    }
    next()
})
const app = createApp(App)
app.use(router)
// app.use(animated)
app.mount('#app')

