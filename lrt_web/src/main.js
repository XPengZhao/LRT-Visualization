import { createApp } from 'vue'
import App from './App.vue'
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js"
import axios from "axios";

axios.get('./config.json').then((result)=>{
    localStorage.setItem('ApiUrl',result.data.ApiUrl);
}).catch((error)=>{console.log(error)})
const app = createApp(App)

app.mount('#app')

