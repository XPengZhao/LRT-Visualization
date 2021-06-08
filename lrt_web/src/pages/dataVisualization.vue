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
        <button type="button" id="recordButton" class="ml-3 btn" style="background-color: #04254E;color: white;min-width: 160px"  data-toggle="button" aria-pressed="false" @click="recording()">
          <img :src="recordimg" style="height: 20px">
          Recording
        </button>
        <vue-slider v-model="indexValue"
                    :width="1000"
                    :lazy="true"
                    @dragging="test"
                    @change="test"
                    :min-range="20"
                    :max-range="200"
                    :max = "timeArrayLength"
                    :tooltip = "'always'"
                    :tooltip-placement="'bottom'"
                    ref="timeSlider"
                    id = "timeSlider"

        />
<!--        <button type="button" id="stopButton" class="ml-3 btn" style="background-color: #04254E;color: white;min-width: 160px"  data-toggle="button" aria-pressed="false" @click="stopConnect()">-->
<!--          <img :src="stopimg" style="height: 20px">-->
<!--          Stop-->
<!--        </button>-->
      </div>
    </div>
    <button type="button"  class="ml-3 btn" style="background-color: #04254E;color: white;min-width: 160px"  data-toggle="button" aria-pressed="false" @click="toAnalysis()">
      Analysis
    </button>
    <button type="button" id="fullButton" class="btn" style="background-color: #04254E;color: white;min-width: 20px;position: relative;right: 0"  data-toggle="button" aria-pressed="false" @click="changeScreen()">
      <img :src="windowSizeImg" style="height: 20px">
    </button>
  </nav>
  <div class="mainBox row mt-3">
    <div class="col-6 mt-2">
      <Localization ref="localization"></Localization>
    </div>
    <div class="col-4">
      <div class="row mt-2">
        <Phase ref="phase"></Phase>
      </div>
      <div class="row mt-2">
        <RSSLine ref="rssline"></RSSLine>
      </div>
      <div class="row mt-2">
        <Spectrum ref="spectrum"></Spectrum>
      </div>
    </div>
    <div class="col-2 ">
      <Panel ref="panel"></Panel>
      <RSS class="mt-2" ref="rss"></RSS>
<!--      <radar class="mt-2" ref="radar"></radar>-->
    </div>

  </div>
  <div id="createTable" class="createTable">
    <div class="tableCard animate__animated animate__backInLeft" id = 'tableCard'>
      <div class="card" style="border: 2px solid #151515">
        <div class="card-header" id="experimentID" style="background-color: #3c415c;color: white;">
          Experiment ID:
        </div>
        <div class="card-body" style="background-color: #b4a5a5;color: #3c415c">
          <div class="row" >
            <input type="file" accept="image/*" v-on:change="uploadImg($event)" v-show="false" id="describeImgArea"/>
            <div class="ml-3 uploadLabel">Upload</div>
            <label id="describeImgPath" class="col-8 uploadPath" style="color: #3c415c"></label>
            <button class="btn uploadButton" v-on:click="callUpImg()">Choose</button>
          </div>
          <hr>
          <div style="width: 100%">
            <h5 class="card-title">Describe</h5>
            <textarea id="describeWord" style="width: 80%;color: black;background-color: rgba(255,255,255,0.17)" rows="5" cols="33" ></textarea>
          </div>
          <hr>
          <button class="btn sendButton" v-on:click="sendTable()">Send</button>
      </div>
    </div>
    </div>
  </div>
</template>
<script>
/* eslint-disable */
import {state} from "@/store/state";
import stomp from 'stompjs';
import parse from 'fast-json-parse';
import {CalendarComponent, GridComponent, LegendComponent, TimelineComponent} from 'echarts/components'
import {CustomChart, EffectScatterChart} from 'echarts/charts';
import axios from "axios";
import Localization from "@/components/Localization";
import Phase from "@/components/Phase";
import RSS from "@/components/Rss";
import Spectrum from "@/components/Spectrum";
import Panel from "@/components/Panel";
import RSSLine from "@/components/rssLine";
import Radar from "@/components/Radar";
import {router} from "@/router";
import screenfull from 'screenfull';
let echarts = require("echarts/lib/echarts");
import  bootbox from 'bootbox'
require("echarts/lib/chart/heatmap")
require('echarts/lib/chart/scatter')
require('echarts/lib/chart/line')
require('echarts/lib/component/title')
require('echarts/lib/component/toolbox')
require('echarts/lib/component/tooltip')
require('echarts/lib/component/visualMap')
echarts.use([GridComponent])
echarts.use([LegendComponent]);
echarts.use([CalendarComponent]);
echarts.use([EffectScatterChart]);
echarts.use([CustomChart]);
echarts.use([TimelineComponent]);


export default {
name: "DrawPictrue",
  components: {Radar, RSSLine, Panel, Spectrum, RSS, Phase, Localization,VueSlider: window['vue-slider-component']},
  data(){
    return{
      recordimg:require('@/assets/recordWhite.png'),
      stopimg:require('@/assets/stop.png'),
      flowerimg:require('@/assets/flower.png'),
      createTable:false,
      isFullscreen: false,
      atnpos:Array,
      receiveNum: 0,
      replayisNull:true,
      indexValue:[0,200],
      timeArrayLength:1000,
    }

  },
  computed:{
    windowSizeImg(){
      return this.isFullscreen?require('@/assets/window.png'):require('@/assets/fullScreen.png')
    },
    // timeArrayLength(){
    //   return
    // }
  },
  mounted () {
    this.init()
    this.isReplay()
    this.uploader_online()
    },
  methods:{
  test(data){
    console.log(data)
  },
    init(){
      this.$refs.localization.initLocalizationCharts()
      this.$refs.phase.initPhaseCharts()
      this.$refs.rss.initRSSCharts()
      this.$refs.spectrum.initSpectrumCharts()
      this.$refs.rssline.initRSSLineCharts()
      // this.$refs.radar.initRadarCharts()
      sessionStorage.setItem('record',0)
      sessionStorage.setItem('createTable',0)
      $('#createTable').hide()
      $('#stopButton').prop('disabled',true)
      $('#recordButton').prop('disabled',true)

    },
    changeScreen(){
      if (!screenfull.isEnabled) return alert(`Error`);
      this.isFullscreen = !this.isFullscreen
      screenfull.toggle();
    },
    isReplay(){
      if(state.queue==='replay'){
        $('#stopButton').hide()
        $('#onlineButton').hide()
        $('#recordButton').hide()
      }else {
        $('#timeSlider').hide()
      }
    },
    recordAble(){
      if(state.queue==='replay'){
        $('#recordButton').addClass('disable')
      }
    },
    recordMessageSend(localData){
      let myDate = new Date()
      let spectrumSave = {
        "algorithm": localData.spectrum.algorithm, // which algorithm is used.
        "confidence": localData.spectrum.confidence,//how many gateways contribute to this spectrum
        "xRange":localData.spectrum.xRange, // searched range
        "yRange":localData.spectrum.yRange, //searched range
        "zRange":localData.spectrum.zRange, //searched range. If z1=z2, the searching is taken on a single plane.
        "aoa":localData.spectrum.aoa,
        "createdTime": localData.spectrum.createdTime,
      }
      axios.post('http://localhost:3000/lrt/insert', {
        table: sessionStorage.getItem('tableName'),
        tagId:localData.tagId,
        logTime:localData.logTime, //the logical time after the queque alignment
        phyTime:localData.phyTime, //the real timestamp created by the xserver
        savedTime:myDate.toLocaleString('chinese', { hour12: false })+':'+myDate.getMilliseconds(), //the timestamp when this data is saved into the database.
        position: localData.position, // the computed position by xserver.
        truth:localData.truth, //computed by optiTrack
        xServer: localData.xServer,
        // spectrum:localData.spectrum
        spectrum:spectrumSave
      })
    },
    realTimeProcessing(data) {
      const that = this
      let rss =that.$refs.rss
      let local = that.$refs.localization
      let phase = that.$refs.phase
      let spectrum = that.$refs.spectrum
      let rssLine = that.$refs.rssline
      // let radar = this.$refs.radar
      let word = data.body
      if (word) {
        try{
          var localData = JSON.parse(word)
        }catch (e) {
          console.log(word)
          console.log(e)
        }

        if (localData.xServer) {
          that.receiveNum++
          // console.log(localData)
          if (sessionStorage.getItem('record') === '1') {
            that.recordMessageSend(localData)
          }
          for (let key in localData.xServer.gateways) {
            state.rss[key] = localData.xServer.gateways[key].rss
            // state.aoa[key] = localData.xServer.gateways[key].aoa[0]
            state.atnpos[key] = localData.xServer.gateways[key].position[0]
            if (key in state.phase) {
              for (let i = 0; i < 16; i++) {
                state.rssLine[key][i].push(localData.xServer.gateways[key].rss[i])
                state.phase[key][i].push(localData.xServer.gateways[key].phase[i])
              }
            } else {
              state.rssLine[key] = localData.xServer.gateways[key].rss.map(function (item){
                return [item]
              })
              state.phase[key] = localData.xServer.gateways[key].phase.map(function (item) {
                return [item]
              })
            }
            data.ack()
          }
          phase.upDatePhase(that.receiveNum)
          rssLine.upDateRSSline(that.receiveNum)
          // radar.upDateRadar()
          let x = localData.position[0]
          let y = localData.position[2]
          local.upDateLocalization([x, y], localData.tagId, localData.truth, localData.spectrum.xRange, localData.spectrum.zRange)
          let spectrumList =[]
          for(let i =0;i<100;i++){
            for(let j=0;j<100;j++){
              spectrumList.push([i,j,localData.spectrum.data[i][j]])
            }
          }
          spectrum.upDateSpectrum(spectrumList)
          rss.upDateRSS()
    }


        }
    },
    uploader_online(){
      $('#stopButton').prop('disabled',false)
      $('#onlineButton').addClass('disabled')
      $('#recordButton').prop('disabled',false)
      const API = localStorage.getItem('ApiUrl')
      this.ws = new WebSocket(API)
      // const ws = new WebSocket('ws://192.168.0.100:15674/ws')
      this.client = stomp.over(this.ws)
      this.client.heartbeat.incoming = 300
      this.client.heartbeat.outgoing = 300
      // this.client.connect('admin','admin',this.onconnect,this.disconnect,'/')
      if(state.queue==='replay'){
        this.client.connect('vueAdmin','vueAdmin',this.onreplay,this.disconnect,'/replay')
      }
      else {
        this.client.connect('admin','admin',this.onconnect,this.disconnect,'/')
      }
    },
    disconnect(e){
      this.uploader_online()
      console.log(e)
      console.log('Reconnect')
    },
    onreplay: function () {
      const that = this
      this.dialog = bootbox.dialog({
        message: '<p class="text-center mb-0"><i class="fa fa-spin fa-cog"></i> Please wait while we do something...</p>',
        closeButton: false
      });
      this.subclient = this.client.subscribe('/queue/replay', function (data) {
        let word = data.body
        let localData = parse(word).value
        for (let key in localData.xServer.gateways) {
          that.replayisNull = false
          if (key in state.rssLine) {
            state.rss[key].push(localData.xServer.gateways[key].rss)
            state.aoa[key].push(localData.spectrum.aoa)
            state.atnpos[key].push(localData.xServer.gateways[key].position[0])
            for (let i = 0; i < 16; i++) {
              state.rssLine[key][i].push(localData.xServer.gateways[key].rss[i])
              state.phase[key][i].push(localData.xServer.gateways[key].phase[i])
            }
          } else {
            state.rss[key] = [localData.xServer.gateways[key].rss]
            state.aoa[key] = [localData.spectrum.aoa]
            state.atnpos[key] = [localData.xServer.gateways[key].position[0]]
            state.rssLine[key] = localData.xServer.gateways[key].rss.map(function (item) {
              return [item]
            })
            state.phase[key] = localData.xServer.gateways[key].phase.map(function (item) {
              return [item]
            })
          }
          data.ack()
        }
        if (localData.end) {
          that.subclient.unsubscribe()
        }
      })
      if (this.replayisNull) {
        setTimeout(this.hideDialog,1000)
        this.subclient.unsubscribe()
      }

    },
    hideDialog(){
      this.dialog.modal('toggle')
    },
    onconnect(){
        this.subclient = this.client.subscribe('/queue/oss.url_test',this.realTimeProcessing)
    },
    convSpectrum(arr,dimension){
      let arr1 = arr.flatMap(function (item){
        return item
      })
      return arr1.map(function (value, index) {
        let x = parseInt(index / dimension)
        let y = index % dimension
        return [x, y, value]
      })
    },
    recording(){
      if(sessionStorage.getItem('record')==='1'){
        $('#recordButton').css({
          'background-color':'#04254E',
          'border':''
        })
        sessionStorage.setItem('record','0')
        $('#experimentID').html('Experiment ID: '+sessionStorage.getItem('tableName'))
        // $('#createTable').addClass('animate__animated','animate__backInLeft')
        $('#tableCard').removeClass('animate__backOutDown')
       $('#createTable').show()
      }else {
        $('#recordButton').css({
          'background-color':'red',
          'border':'2px solid white'
        })
        let time = new Date()
        sessionStorage.setItem('tableName',time.toLocaleString('chinese', { hour12: false }))
        sessionStorage.setItem('record','1')
      }
    },
    sendTable(){
      const that = this

      let a = that.valueURL
      axios.post('http://localhost:3000/lrt/insertTable',{
        Describe:$('#describeWord').val(),
        img:a,
        tableName:sessionStorage.getItem('tableName'),
      }).then(function (){
        that.valueURL = 'null'
        $('#describeWord').val('')
        sessionStorage.setItem('tableName','')
      });
      setTimeout(function (){
        $('#tableCard').addClass('animate__backOutDown')
      },1000)
    },
    stopConnect(){
      $('#stopButton').prop('disabled',true)
      $('#recordButton').prop('disabled',true)
      $('#onlineButton').removeClass('disabled')
      state.rss={}
      state.phase={}
      state.rssLine={}
      state.aoa={}
      state.gatewayChoose='gateway1'
      state.queue='oss.url_test'
      if(this.client){
        this.client.unsubscribe('0')
      }
      this.refresh()
    },
    callUpImg(){
      $('#describeImgArea').click()
    },
    uploadImg(e){
      const that = this
      let file = e.target.files[0]
      var reader = new FileReader()
      reader.readAsDataURL(file)
      reader.onload = function (){
        that.valueURL = this.result
      }
      $('#describeImgPath').html(file.name)
    },
    refresh(){
      this.$refs.localization.refreshChart()
      this.$refs.panel.refreshCharts()
      this.$refs.phase.refreshChart()
      this.$refs.radar.refreshChart()
      this.$refs.rss.refreshCharts()
      this.$refs.rssline.refreshRssline()
      this.$refs.spectrum.refreshSpectrum()
    },
    toHome(){
      this.stopConnect()
      state.rss={}
      state.phase={}
      state.rssLine={}
      state.aoa={}
      state.gatewayChoose='gateway1'
      state.queue='oss.url_test'
      router.push({
        name: 'home'
      })
    },
    toAnalysis(){
    this.stopConnect()
      router.push({
        name: 'Analysis'
      })
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
.createTable{
  overflow: hidden;
  font-family: 'Ubuntu', sans-serif;
  width: 600px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
  z-index: 999;

}
.tableCard{
  font-weight: 700;
  text-align: center;
}
.uploadLabel{
  height:40px;
  width:80px;
  text-align: center;
  line-height:40px;
  background-color: #3c415c;
  border-radius: 5px;
  color: white
}
.uploadButton{
  background-color: #3c415c;
  border-radius: 5px;
  color: white;
  height:40px;
}
.uploadPath{
  color: #3c415c;
  height:40px;
  text-align: center;
  line-height:40px;
  border-bottom: 1px solid #151515;
}
.sendButton{
  width: 100px;
  color: white;
  background-color: #3c415c;
  border-radius: 5px;
}
</style>
