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
  <div class="mainBox row mt-3">
    <div class="col-4 mt-2">
      <Cdf ref="cdf"></Cdf>
      <ConfidenceCdf class="mt-5" ref="confidenceCdf"></ConfidenceCdf>
    </div>
    <div class="col-4">
      <div class="row mt-2">
        <error-bar ref="errorBar"></error-bar>
      </div>
      <div class="row mt-2">
        <Route ref="route"></Route>
      </div>
      <div class="row mt-2">
      </div>
    </div>
    <div class="col-2 ">
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
import stomp from "stompjs";
import bootbox from "bootbox";
import parse from "fast-json-parse";
import Route from "@/components/Route";
const cdf = require('cumulative-distribution-function');
export default {
  name: "distanceError",
  components: {Route, ErrorBar, ConfidenceCdf, Cdf},
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

  mounted() {
    this.$refs.confidenceCdf.initConfidenceCdfCharts()
    this.$refs.cdf.initCdfCharts()
    this.$refs.errorBar.initErrorBarCharts()
    this.$refs.route.initRouteCharts()
    this.uploader_online()
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
    stopConnect(){
      this.client.disconnect()
    },
    toHome(){
      this.stopConnect()
      router.push({
        name: 'home'
      })
    },
    toShow(){
      this.stopConnect()
      router.push({
        name: 'Show'
      })
    },
    uploader_online(){
      // this.ws = new WebSocket(this.MQUrl)
      const ws = new WebSocket('http://158.132.255.123:15674/ws')
      this.client = stomp.over(ws)
      this.client.heartbeat.incoming = 1000
      this.client.heartbeat.outgoing = 10000
      // this.client.connect('admin','admin',this.onconnect,this.disconnect,'/')
      this.client.connect('admin','admin',this.onreplay,this.disconnect,'/')
    },
    disconnect(e){
      console.log(e)
    },
    onreplay: function () {
      const that = this
      if(!this.dialog){
        this.dialog = bootbox.dialog({
          message: '<p class="text-center mb-0"><i class="fa fa-spin fa-cog"></i> Please wait while we do something...</p>',
          closeButton: false
        });
      }
      this.subclient = this.client.subscribe('/queue/replay', function (data) {
        let word = data.body
        let localData = parse(word).value
        // console.log(localData)
        that.errorNum = that.distanceCompute(localData.truth[0],localData.position[0],localData.truth[2],localData.position[2])
        state.error.push(that.errorNum)
        state.replay.truth.push([localData.truth[0],localData.truth[2]])

        state.replay.position.push([localData.position[0],localData.position[2]])
        if(localData.spectrum[0].confidence in state.confidence){
          state.confidence[localData.spectrum[0].confidence].push(that.errorNum)
        }else {
          state.confidence[localData.spectrum[0].confidence] = [that.errorNum]
        }
      if(that.errorNum<5){
        that.errorBarData.push([Number(localData.truth[0]),Number(localData.truth[2]),that.errorNum])
      }
      that.groundTruth.push([localData.truth[0],localData.truth[2]])
        if (localData.end) {
          that.hideDialog()
          that.subclient.unsubscribe()
          that.updateChart()
        }
      })

    },
    hideDialog(){
      this.dialog.modal('toggle')
    },
    updateChart(){
      console.log(state.error)
      this.mycdf = cdf(state.error)
      this.$refs.cdf.updateChart(this.mycdf)
      let ccdf = {}
      for(let key in state.confidence){
        ccdf[key] = cdf(state.confidence[key])
      }
      this.$refs.confidenceCdf.updateCharts(ccdf)
      this.$refs.errorBar.updateChart(this.errorBarData)
      this.$refs.route.updateChart(this.groundTruth)
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
