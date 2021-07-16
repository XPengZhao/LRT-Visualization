<template>
    <nav class="navbar navbar-expand-lg" style="background-color: #04254E;">
      <a class="navbar-brand" href="#"  style=" color: white;" @click="toHome()">
        <img :src="flowerimg" style="height: 30px">
        Chrysanth LRT
      </a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
        </div>
      </div>
      <button type="button" id="recordButton" class="ml-3 btn" style="background-color: #04254E;color: white;min-width: 160px"  data-toggle="button" aria-pressed="false" @click="toShow()">
        <img :src="backImg" style="height: 20px">
        Back
      </button>
      <button type="button" id="fullButton" class="btn" style="background-color: #04254E;color: white;min-width: 20px;position: relative;right: 0"  data-toggle="button" aria-pressed="false" @click="changeScreen()">
        <img :src="windowSizeImg" style="height: 20px">
      </button>
    </nav>
  <div class="mainBox">
    <div class="row mt-2" style="width: 100%;  margin:0 auto;">
      <span style="width: 2.5%"></span>
      <Route  style="width: 30%" ref="route"></Route>
      <span style="width: 2.5%"></span>
      <routeError style="width: 30%" ref="routeError"></routeError>
      <span style="width: 2.5%"></span>
      <error-bar style="width: 30%" ref="errorBar"></error-bar>
      <span style="width: 2.5%"></span>
    </div>
    <div class="row mt-2" style="width: 100%;  margin:0 auto;">
      <span style="width: 2.5%;z-index: -50"></span>
      <Cdf style="width: 45.8%" ref="cdfChart"></Cdf>
      <span style="width: 2.7%"></span>
      <ConfidenceCdf style="width: 45.8%" ref="confidenceCdf"></ConfidenceCdf>
      <span style="width: 2.5%"></span>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import {router} from "@/router";
import screenfull from "screenfull";
import ConfidenceCdf from "../components/confidenceCdf";
import Cdf from "../components/Cdf"
import {state} from "../store/state";
import ErrorBar from "../components/confidenceBar";
import Route from "@/components/Route";
import routeError from "../components/routeError";
import axios from "axios";
import {onMounted,ref} from "vue";


export default {
  name: "distanceError",
  components: {Route, ErrorBar, ConfidenceCdf, Cdf, routeError},
  data(){
    return{
      backImg:require('@/assets/backArrow.png'),
      flowerimg:require('@/assets/flower.png'),
      isFullscreen: false,
      isUpdate:true,
      errorBarData:[],
      groundTruth:[],

    }
  },
  computed: {
    windowSizeImg() {
      return this.isFullscreen ? require('@/assets/window.png') : require('@/assets/fullScreen.png')
    },
  },
  setup(){
    var isFullscreen = false
    const cdf = require('cumulative-distribution-function');
    const BackendUrl=localStorage.getItem("BackendUrl")
    const cdfChart = ref()
    const confidenceCdf = ref()
    const errorBar = ref()
    const route = ref()
    const routeError = ref()
    onMounted(()=>{
      confidenceCdf.value.initConfidenceCdfCharts()
      cdfChart.value.initCdfCharts()
      errorBar.value.initErrorBarCharts()
      route.value.initRouteCharts()
      routeError.value.initRouteErrorCharts()
      init()
      // setInterval(init,10000)
    })
    const errorBarData=((min,max)=>{
      let arr = []
      for(let i=min-10;i<max+10;i++){
        arr.push(i)
      }
      return arr
    })
    const init=(()=>{
      console.log()
      if(sessionStorage.getItem('tableName')){
        const that = this
        axios.post(BackendUrl+'/analysis',{
          table:sessionStorage.getItem('tableName')
        }).then(function (res) {
          state.error = res.data.error
          state.confidence = res.data.confidence
          state.truthError = res.data.truthError
          state.truthConfidence = res.data.truthConfidence
          state.cdfIndex = res.data.index
          state.ccdfIndex = res.data.ccdfIndex
          // console.log(state.ccdfIndex)
          // console.log(state.confidence)
          state.routeOpition.xAxis.data = errorBarData(res.data.truthMinX,res.data.truthMaxX)
          state.routeOpition.yAxis.data = errorBarData(res.data.truthMinY,res.data.truthMaxY)
          state.routeErrorOpition.xAxis.data = errorBarData(res.data.truthMinX,res.data.truthMaxX)
          state.routeErrorOpition.yAxis.data = errorBarData(res.data.truthMinY,res.data.truthMaxY)
          state.truthArray = res.data.truthArray
          state.groundTruth = res.data.groundTruth
          state.round = res.data.round
          state.roundp = res.data.roundp
          state.roundr1 = res.data.roundr1
          state.confidenceTruth = res.data.confidenceTruth
          updateChart()
        })
      }
    })
    const distanceCompute=((x1,x2,y1,y2)=>{
      let a = Math.pow((x1-x2),2)
      let b = Math.pow((y1-y2),2)
      return Number(Math.sqrt(a+b).toFixed(2))
    })
    const changeScreen=(()=>{
      if (!screenfull.isEnabled) return alert(`Error`);
      this.isFullscreen = !this.isFullscreen
      screenfull.toggle();
    })
    const toHome=(()=>{
      sessionStorage.setItem('tableName','')
      router.push({
        name: 'home'
      })
    })
    const toShow=(()=>{
      state.atnPos={}
      state.atnR=0
      state.error=[]
      state.confidence={}
      state.truthError=[]
      state.truthConfidence=[]
      state.cdfIndex=[]
      state.ccdfIndex=[]
      state.truthArray=[]
      state.groundTruth={}
      state.round={}
      state.roundp=[]
      state.oneMeterRound=[]
      state.atnRound=[]
      router.push({
        name: 'dataList'
      })
    })
    const updateChart=(()=>{
      let mycdf = cdf(state.error)
      cdfChart.value.updateChart(mycdf)
      let ccdf = {}
      for(let key in state.confidence){
        if(key!=='0'){
          ccdf[key] = cdf(state.confidence[key])
        }
      }
      confidenceCdf.value.updateCharts(ccdf)
      errorBar.value.updateChart()
      route.value.updateChart()
      routeError.value.updateChart()
    })

    return { init,errorBarData,BackendUrl,distanceCompute,changeScreen,toHome,toShow,cdfChart,confidenceCdf,route,routeError,errorBar,updateChart,isFullscreen}
  },
}
</script>

<style scoped>
.mainBox{
  margin: 0 auto;
  min-height: 80px;
  width: 100%;
  position:relative;
  z-index:5;
  top:0;

}
</style>
