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
        <div class="dropdown">
          <button class="btn" style="background-color: #04254E;color: white;min-width: 160px" type="button" v-on:click="test()">
            test
          </button>
          <button class="btn" style="background-color: #04254E;color: white;min-width: 160px" type="button" v-on:click="uploader_online()">
            <img :src="connectimg" style="height: 20px;">
            Connect
          </button>
<!--          <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">-->
<!--            <a class="dropdown-item" data-disabled="true" data-toggle="dropdown" id="onlineButton" href="#" >Now</a>-->
<!--            <hr>-->
<!--            <a class="dropdown-item" data-disabled="true" data-toggle="dropdown" href="#" v-on:click="callUpArea()">Local</a>-->
<!--            <hr>-->
<!--            <a class="dropdown-item" data-disabled="true" data-toggle="dropdown"  href="#" @click="toDataList">DataList</a>-->
<!--          </div>-->
        </div>
        <button type="button" id="recordButton" class="ml-3 btn" style="background-color: #04254E;color: white"  data-toggle="button" aria-pressed="false" @click="recording()">
          <img :src="recordimg" style="height: 20px">
          Recording
        </button>
        <button type="button" id="stopButton" class="ml-3 btn" style="background-color: #04254E;color: white"  data-toggle="button" aria-pressed="false" @click="stopConnect()">
          <img :src="stopimg" style="height: 20px">
          Stop
        </button>
      </div>
    </div>
  </nav>
  <input type="file" v-on:change="uploader($event)" webkitdirectory directory v-show="false" id="uparea"/>
  <div class="mainBox row mt-5">
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
      <radar class="mt-2" ref="radar"></radar>

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
import stomp from 'stompjs'
import parse from 'fast-json-parse'
import {CalendarComponent, GridComponent, LegendComponent, TimelineComponent} from 'echarts/components'
import {CustomChart, EffectScatterChart} from 'echarts/charts';
import axios from "axios";
import Localization from "@/components/Localization";
import Phase from "@/components/Phase";
import RSS from "@/components/RSS";
import Spectrum from "@/components/Spectrum";
import Panel from "@/components/Panel";
import RSSLine from "@/components/RSSLine";
import Radar from "@/components/radar";
import {router} from "@/router";

let echarts = require("echarts/lib/echarts");
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
  components: {Radar, RSSLine, Panel, Spectrum, RSS, Phase, Localization},
  data(){
    return{
      connectimg:require('@/assets/connect.png'),
      recordimg:require('@/assets/recordWhite.png'),
      stopimg:require('@/assets/stop.png'),
      flowerimg:require('@/assets/flower.png'),
      files: {},
      num : 0,
      createTable:false,
      valueURL:'',
      timestamp:'',
      timeSort:true,
    }

  },
  mounted () {

    this.$refs.localization.initLocalizationCharts()
    this.$refs.phase.initPhaseCharts()
    this.$refs.rss.initRSSCharts()
    this.$refs.spectrum.initSpectrumCharts()
    this.$refs.rssline.initRSSLineCharts()
    this.$refs.radar.initRadarCharts()
    sessionStorage.setItem('record',0)
    sessionStorage.setItem('createTable',0)
    $('#createTable').hide()
    $('#stopButton').prop('disabled',true)
    $('#recordButton').prop('disabled',true)
    },
  methods:{

    callUpArea(){
      $("#uparea").click()
    },
      uploader(es){
      this.files = es.target.files
      for (let i =0; i < this.files.length; i++) {
        setTimeout(this.loadfile, (i+1)*1000,i)
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
      this.client.heartbeat.incoming = 100
      this.client.heartbeat.outgoing = 100000
      this.client.connect('admin','admin',this.onconnect,this.disconnect,'/')
    },
    disconnect(){
      console.log('error')
    },
    onconnect(){
      let rss =this.$refs.rss
      let local = this.$refs.localization
      let phase = this.$refs.phase
      let spectrum = this.$refs.spectrum
      let rssline = this.$refs.rssline
      let radar = this.$refs.radar
      const that = this
     this.subclient = this.client.subscribe('/queue/oss.url_test',function (data){
       let word = data.body
       let localData = parse(word).value
       if(that.timestamp){
         that.timeSort = Number(that.timestamp) - Number(localData['fuse'].timestamp) < 0;
       }else {
         that.timestamp = localData['fuse'].timestamp
       }
       that.timestamp = localData['fuse'].timestamp
       if(sessionStorage.getItem('record')==='1'&&that.timeSort){

             axios.post('http://localhost:3000/lrt/insert',{
               table:sessionStorage.getItem('tableName'),
               time: localData.time,
               tagid: localData.tagid,
               atnpos: localData.atnpos,
               phase: localData.phase,
               rss: localData.rss,
               pos: localData.pos,
               // rn16:Array,
             })
           for(let key in localData){
             if(key in state.rss){
               state.rss[key] = localData[key].rss
               state.aoa[key] = localData[key].aoa
               for(let i = 0;i < 16; i++){
                 if(state.rssLine[key][i]){
                   state.rssLine[key][i].push(localData[key].rss[i])
                 }else {
                   state.rssLine[key][i] = [localData[key].rss[i]]
                 }
                 if(state.phase[key][i]){
                   state.phase[key][i].push(localData[key].phase[i])
                 }else {
                   state.phase[key][i] = [localData[key].phase[i]]
                 }
               }
             }
           }


       }

       rss.upDateRSS()
       phase.upDatePhase()
       rssline.upDateRSSline()
       radar.upDateRadar()
       let x = localData['fuse'].pos[0]
       let y = localData['fuse'].pos[1]
       local.upDateLocalization([x, y], localData['fuse'].tagid,localData['fuse'].atnpos)
       if (localData['fuse'].spectrum) {
         let spectrumList = that.convSpectrum(localData['fuse'].spectrum,100)
         spectrum.upDateSpectrum(spectrumList)
       }
     })
    },
    convSpectrum(arr,dimension){
      let arr1 = arr.flatMap(function (item){
        return item
      })
      return arr1.map(function (value, index) {
        let x = parseInt((index + 1) / dimension)
        let y = (index + 1) % dimension
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
      $('#tableCard').addClass('animate__backOutDown')
      let a = that.valueURL
      axios.post('http://localhost:3000/lrt/insertTable',{
        antPos:[],
        Describe:$('#describeWord').val(),
        img:a,
        tableName:sessionStorage.getItem('tableName'),
      }).then(function (){
        that.valueURL = 'null'
        $('#describeWord').val('')
        sessionStorage.setItem('tableName','')
      });
    },
    stopConnect(){
      $('#stopButton').prop('disabled',true)
      $('#recordButton').prop('disabled',true)
      $('#onlineButton').removeClass('disabled')
      this.timestamp = ''
      this.timeSort = true
      if(this.subclient){
        this.subclient.unsubscribe()
      }
      if (this.ws){
        this.ws.close()
      }
      this.$refs.localization.refreshChart()
      this.$refs.panel.refreshCharts()
      this.$refs.phase.refreshChart()
      this.$refs.radar.refreshChart()
      this.$refs.rss.refreshCharts()
      this.$refs.rssline.refreshRssline()
      this.$refs.spectrum.refreshSpectrum()
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
    toDataList(){
        router.push({
          name: 'dataList'
        })
    },
    toHome(){
      this.stopConnect()
      router.push({
        name: 'home'
      })
    },
  }
}

</script>

<style scoped>
.mainBox{
  margin: 0 auto;
  min-height: 1300px;
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
