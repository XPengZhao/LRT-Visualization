<template>
  <nav class="navbar navbar-expand-lg" style="background-color: #04254E;">
    <a class="navbar-brand" href="#"  style=" color: white;">LRT</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <div class="dropdown">
          <button class="btn dropdown-toggle" style="background-color: #04254E;color: white" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <img :src="connectimg" style="height: 20px;">
            Connect
          </button>
          <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <a class="dropdown-item" href="#" v-on:click="uploader_online()">Now</a>
            <hr>
            <a class="dropdown-item" href="#" v-on:click="callUpArea()">Local</a>
            <hr>
            <a class="dropdown-item" href="#" v-on:click="test()">test</a>
          </div>
        </div>
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
      <Panel></Panel>
      <RSS class="mt-2" ref="rss"></RSS>
      <radar class="mt-2" ref="radar"></radar>

    </div>
  </div>

</template>

<script>
import $ from "jquery"
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
import { TimelineComponent } from 'echarts/components';
import Localization from "@/components/Localization";
import Phase from "@/components/Phase";
import RSS from "@/components/RSS";
import Spectrum from "@/components/Spectrum";
import Panel from "@/components/Panel";
import RSSLine from "@/components/RSSLine";
import Radar from "@/components/radar";

echarts.use([TimelineComponent]);
export default {
name: "DrawPictrue",
  components: {Radar, RSSLine, Panel, Spectrum, RSS, Phase, Localization},
  data(){
    return{
      connectimg:require('@/assets/connect.png'),
      files: {},
      num : 0,
      webpath: 'ws://10.11.15.93:15674/ws'
    }

  },
  mounted () {
    this.$refs.localization.initLocalizationCharts()
    this.$refs.phase.initPhaseCharts()
    this.$refs.rss.initRSSCharts()
    this.$refs.spectrum.initSpectrumCharts()
    this.$refs.rssline.initRSSLineCharts()
    this.$refs.radar.initRadarCharts()
    },
  methods:{
    testradar(r,t){
      let radar = this.$refs.radar
      radar.upDateRadar([[r, t]])
    },
    test(){
      for (var i = 0; i <= 100; i++) {
        var theta = Math.random();
        var r = theta*50
        setTimeout(this.testradar,(i+1)*1000,theta,r)
      }

    },
    callUpArea(){
      if(this.subclient){
        this.subclient.unsubscribe()
      }
      $("#uparea").click()
      // location.reload()
      // this.subclient.unsubscribe()

    },
    uploader(es) {
      this.files = es.target.files
      this.$refs.radar.connect = true
      for (let i =0; i < this.files.length; i++) {
        setTimeout(this.loadfile, (i+1)*1000,i)
      }
    },
    uploader_online() {
      this.$refs.radar.connect = true
      const API = localStorage.getItem('ApiUrl')
      const ws = new WebSocket(API)
      // const ws = new WebSocket('ws://192.168.0.100:15674/ws')
      this.client = stomp.over(ws)
      this.client.heartbeat.incoming = 0
      this.client.heartbeat.outgoing = 20000
      this.client.connect('admin','admin',this.onconnect,this.disconnect,'/')
    },
    disconnect() {
      console.log('error')
    },
    onconnect() {
      let rss =this.$refs.rss
      let local = this.$refs.localization
      let phase = this.$refs.phase
      let spectrum = this.$refs.spectrum
      let rssline = this.$refs.rssline
     this.subclient = this.client.subscribe('/queue/oss.url_test',function (data){
       let middata = []
       let word = data.body
       let localData = parse(word).value
         for (let i = 0; i < 4; i++) {
           for (let j = 0; j < 4; j++) {
             let num = Number(localData.rss[i * 4 + j])
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
    ,
    loadfile(num){
      let rss =this.$refs.rss
      let local = this.$refs.localization
      let phase = this.$refs.phase
      let spectrum = this.$refs.spectrum
      let rssline = this.$refs.rssline
      let reader = new FileReader()
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





</style>
