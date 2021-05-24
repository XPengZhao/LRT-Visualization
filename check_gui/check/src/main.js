import { createApp } from 'vue'
import App from './App.vue'
// eslint-disable-next-line
import $ from 'jquery'
import "bootstrap";
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.js"
import axios from "axios";
// eslint-disable-next-line
import 'animate.css';
axios.get('./config.json').then((result)=>{
    localStorage.setItem('ApiUrl',result.data.ApiUrl);
}).catch((error)=>{console.log(error)})
const app = createApp(App)
app.use($)
app.mount('#app')
