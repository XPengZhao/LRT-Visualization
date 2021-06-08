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
    <div class="col-6 mt-2">
      <error-line ref="errorLine"></error-line>
      <Cdf ref="cdf"></Cdf>
    </div>
    <div class="col-4">
      <div class="row mt-2">
      </div>
      <div class="row mt-2">
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
import ErrorLine from "../components/errorLine";
import Cdf from "../components/Cdf"
import stomp from "stompjs";
import parse from "fast-json-parse";
import {state} from "../store/state";
export default {
  name: "distanceError",
  components: {ErrorLine, Cdf},
  data(){
    return{
      backImg:require('@/assets/backArrow.png'),
      flowerimg:require('@/assets/flower.png'),
      isFullscreen: false,
    }
  },
  computed: {
    windowSizeImg() {
      return this.isFullscreen ? require('@/assets/window.png') : require('@/assets/fullScreen.png')
    },
  },
  mounted() {
    this.$refs.errorLine.initErrorLineCharts()
    this.$refs.cdf.initCdfCharts()
    this.uploader_online()
  },
  methods:{
    changeScreen(){
      if (!screenfull.isEnabled) return alert(`Error`);
      this.isFullscreen = !this.isFullscreen
      screenfull.toggle();
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
      const API = localStorage.getItem('ApiUrl')
      this.ws = new WebSocket(API)
      // const ws = new WebSocket('ws://192.168.0.100:15674/ws')
      this.client = stomp.over(this.ws)
      this.client.heartbeat.incoming = 10000
      this.client.heartbeat.outgoing = 10000
      // this.client.connect('admin','admin',this.onconnect,this.disconnect,'/')
      this.client.connect('admin','admin',this.onconnect,this.disconnect,'/')
    },
    disconnect(e){
      // this.uploader_online()
      console.log(e)
    },
    onconnect(){
      const that = this
      this.subclient = this.client.subscribe('/queue/oss.url_test',function (data) {
        let word = data.body
        let localData = parse(word).value
        let error = that.distanceCompute(localData.truth[0],localData.position[0],localData.truth[2],localData.position[2])
        let dayTime = localData.phyTime.split(' ')
        that.$refs.errorLine.updateCharts(dayTime[1],error)

      })
    },
    distanceCompute(x1,x2,y1,y2){
      let a = Math.pow((x1-x2),2)
      let b = Math.pow((y1-y2),2)
      return Math.sqrt(a+b).toFixed(2)
    },
    stopConnect(){
      if(this.client){
        this.client.unsubscribe('0')
      }
    },
  }
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