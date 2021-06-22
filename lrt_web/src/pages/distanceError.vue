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
    <div class="row">
      <Route  class="col-3" ref="route"></Route>
      <routeError class="col-3" ref="routeError"></routeError>
      <error-bar class="col-3" ref="errorBar"></error-bar>
    </div>
    <div class="row">
      <Cdf class="col-5" ref="cdf"></Cdf>
      <ConfidenceCdf class="col-5" ref="confidenceCdf"></ConfidenceCdf>
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
import ErrorBar from "../components/errorBar";
import Route from "@/components/Route";
import routeError from "../components/routeError";
const cdf = require('cumulative-distribution-function');
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
      BackendUrl:localStorage.getItem("BackendUrl")
    }
  },
  computed: {
    windowSizeImg() {
      return this.isFullscreen ? require('@/assets/window.png') : require('@/assets/fullScreen.png')
    },
  },

  mounted() {
    this.$refs.confidenceCdf.initConfidenceCdfCharts()
    this.$refs.cdf.initCdfCharts()
    this.$refs.errorBar.initErrorBarCharts()
    this.$refs.route.initRouteCharts()
    this.$refs.routeError.initRouteErrorCharts()
    this.updateChart()
  },
  methods:{
    distanceCompute(x1,x2,y1,y2){
      let a = Math.pow((x1-x2),2)
      let b = Math.pow((y1-y2),2)
      return Number(Math.sqrt(a+b).toFixed(2))
    },
    changeScreen(){
      if (!screenfull.isEnabled) return alert(`Error`);
      this.isFullscreen = !this.isFullscreen
      screenfull.toggle();
    },
    toHome(){
      router.push({
        name: 'home'
      })
    },
    toShow(){
      router.push({
        name: 'Show'
      })
    },
    updateChart(){
      let mycdf = cdf(state.error)
      this.$refs.cdf.updateChart(mycdf)
      let ccdf = {}
      for(let key in state.confidence){
        if(key!=='0'){
          ccdf[key] = cdf(state.confidence[key])
        }
      }
      this.$refs.confidenceCdf.updateCharts(ccdf)
      this.$refs.errorBar.updateChart()
      this.$refs.route.updateChart()
      this.$refs.routeError.updateChart()
    },
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
