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
          <button class="btn dropdown-toggle" style="background-color: #04254E;color: white;min-width: 160px" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <img :src="connectimg" style="height: 20px;">
            Connect
          </button>
          <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <a class="dropdown-item" data-disabled="true" data-toggle="dropdown" id="onlineButton" href="#" v-on:click="uploader_online()">Now</a>
            <hr>
            <a class="dropdown-item" data-disabled="true" data-toggle="dropdown" href="#" v-on:click="callUpArea()">Local</a>
            <hr>
            <a class="dropdown-item" data-disabled="true" data-toggle="dropdown"  href="#" @click="toDataList">DataList</a>
          </div>
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
let echarts = require("echarts/lib/echarts");
import stomp from 'stompjs'
import parse from 'fast-json-parse'
require("echarts/lib/chart/heatmap")
require('echarts/lib/chart/scatter')
require('echarts/lib/chart/line')
require('echarts/lib/component/title')
require('echarts/lib/component/toolbox')
require('echarts/lib/component/tooltip')
require('echarts/lib/component/visualMap')
import { GridComponent } from 'echarts/components'
echarts.use([GridComponent])
import { LegendComponent } from 'echarts/components';
echarts.use([LegendComponent]);
import { CalendarComponent } from 'echarts/components';
echarts.use([CalendarComponent]);
import { EffectScatterChart } from 'echarts/charts';
echarts.use([EffectScatterChart]);
import { CustomChart } from 'echarts/charts';
echarts.use([CustomChart]);
import axios from "axios";
import { TimelineComponent } from 'echarts/components';
echarts.use([TimelineComponent]);
import Localization from "@/components/Localization";
import Phase from "@/components/Phase";
import RSS from "@/components/RSS";
import Spectrum from "@/components/Spectrum";
import Panel from "@/components/Panel";
import RSSLine from "@/components/RSSLine";
import Radar from "@/components/radar";
import {router} from "@/router";


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
      webpath: 'ws://10.11.15.93:15674/ws',
      createTable:false,
      valueURL:''
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
      uploader(){
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
      const ws = new WebSocket(API)
      // const ws = new WebSocket('ws://192.168.0.100:15674/ws')
      this.client = stomp.over(ws)
      this.client.heartbeat.incoming = 0
      this.client.heartbeat.outgoing = 20000
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
     this.subclient = this.client.subscribe('/queue/oss.url_test',function (data){
       let word = data.body
       let localData = parse(word).value
       if(sessionStorage.getItem('record')==='1'){
         axios.post('http://localhost:3000/lrt/insert',{
           table:sessionStorage.getItem('tableName'),
           time: localData.time,
           tagid: localData.tagid,
           atnid: localData.atnid,
           phase: localData.phase,
           rss: localData.rss,
           pos: localData.pos,
           // rn16:Array,
         }).then(function (){
           if(sessionStorage.getItem('createTable')==='0'){
             sessionStorage.setItem('createTable','1')
           }
         }).catch(function () {
           sessionStorage.setItem('createTable','0')
         });
       }
         rss.upDateRSS(localData.rss)
         let x = localData.pos[0]
         let y = localData.pos[1]
         local.upDateLocalization([x, y], localData.tagid)
         phase.upDatePhase(localData.phase)
         rssline.upDateRSSline(localData.rss)
         radar.upDateRadar([localData.aoa])
         let spectrumList = []
         if (localData.spectrum) {
           for (let i = 0; i < 100; i++) {
             for (let j = 0; j < 100; j++) {
               spectrumList.push([i, j, localData.spectrum[i][j]])
             }
           }
           spectrum.upDateSpectrum(spectrumList)
         }
     })
    },
    loadfile(){
      let rss =this.$refs.rss
      let local = this.$refs.localization
      let phase = this.$refs.phase
      let spectrum = this.$refs.spectrum
      let rssline = this.$refs.rssline
      let reader = new FileReader()
      let num = 0
      reader.readAsDataURL(this.files[num])
      reader.onloadend = function (e) {
      $.getJSON(e.target.result).done(function (localData) {
        let middata = []
        for (let i = 0; i < 4; i++) {
          for (let j = 0; j < 4; j++) {
            let num = localData.rss[i * 4 + j]
            middata.push([i, j, num.toFixed(2)])
          }
        }
        let rssdata = middata.map(function (item) {
          return [item[1], item[0], item[2] || '-'];
        })
        rss.upDateRSS(rssdata)
        let x = localData.pos[0]
        let y = localData.pos[1]
        local.upDateLocalization([x, y], localData.tagid)
        phase.upDatePhase(localData.phase)
        rssline.upDateRSSline(localData.rss)
        let spectrumList = []
        if (localData.spectrum) {
          for (let i = 0; i < 100; i++) {
            for (let j = 0; j < 100; j++) {
              spectrumList.push([i, j, localData.spectrum[i][j]])
            }
          }
          spectrum.upDateSpectrum(spectrumList)
        }
      })
    }
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
      if(this.subclient){
        this.subclient.unsubscribe()
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
