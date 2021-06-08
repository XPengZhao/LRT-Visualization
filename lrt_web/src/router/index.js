import {  createRouter,createWebHashHistory } from 'vue-router'
const dataList = () => import('@/pages/dataList')
const show = () => import('@/pages/dataVisualization')
const home = () => import('@/pages/index')
const analysis = () => import('@/pages/distanceError')
const routes = [
    {
        path: "/",
        name:'home',
        component: home,
        meta:{
            title:'Chrysanth LRT'
        }
        },
    {
        path:'/datalist',
        name:'dataList',
        component: dataList,
        meta:{
            title:'Data List'
        }
    },
    {
        path:'/show',
        name:'Show',
        component: show,
        meta:{
            title:'Show'
        }
    },
    {
        path:'/analysis',
        name:'Analysis',
        component: analysis,
        meta:{
            title:'Analysis'
        }
    },

]
export const router = createRouter({
    history: createWebHashHistory(),
    routes: routes
})
