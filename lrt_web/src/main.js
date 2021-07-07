import { createApp } from 'vue'
import App from './App.vue'
// eslint-disable-next-line
import $ from 'jquery'
import "bootstrap";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js";
import axios from "axios";
import 'animate.css';
import VueSlider from 'vue-slider-component'
import 'vue-slider-component/theme/default.css'
import {router} from "@/router";
import * as echarts from 'echarts';



axios.get('./config.json').then((result)=>{
    localStorage.setItem("BackendUrl",result.data.BackendUrl)
    localStorage.setItem("MQUrl",result.data.MQUrl)
}).catch((error)=>{console.log(error)})
router.beforeEach((to,from,next)=>{
    if(to.meta.title){
        document.title=to.meta.title
    }
    next()
})

const app = createApp(App)
app.use(router)
app.component('VueSlider',VueSlider)
app.config.globalProperties.echarts = echarts;
// app.use(animated)
app.mount('#app')

