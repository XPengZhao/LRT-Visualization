<template>
  <div class="panels mr-3">
    <div style="width:100%;height:100%" ref="rsslinechart"></div>
    <div class="panels-foot"></div>
  </div>
</template>

<script>
import {state} from "@/store/state";
let echarts = require("echarts/lib/echarts");
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
import { TimelineComponent } from 'echarts/components';
echarts.use([TimelineComponent]);
export default {
name: "RSSLine",
  data(){
    return{
      selected : Array(),
      timeArray:[],
    }
  },
  methods:{
    initRSSLineCharts () {
      this.RSSLineChart = echarts.init(this.$refs.rsslinechart,'dark');
      this.RSSLineChart.setOption(state.rsslineOpition)
      window.addEventListener("resize",()=>{
        this.RSSLineChart.resize()
      })
    },
    upDateRSSline(){
      if(state.rssLine[state.gatewayChoose]) {
        for (let key in state.rss) {
          if (state.rssLine[key][0].length > 200) {
            for (let i = 0; i < 16; i++) {
              state.rssLine[key][i].shift()
            }
          }
        }
      let timeArray = this.randArray(state.rssLine[state.gatewayChoose].length)
        for (let i = 0; i < 16; i++) {
          if (state.antselect[i]) {
            state.rsslineOpition.series[i] = {
              name: 'RSS' + String(i + 1),
              type: 'line',
              symbol: 'none',
              // stack: 'rss',
              data: state.rssLine[state.gatewayChoose][i]
            }
          } else {
            state.rsslineOpition.series[i] = {
              name: 'RSS' + String(i + 1),
              type: 'line',
              symbol: 'none',
              data: []
            }
          }
        }

        state.rsslineOpition.xAxis.data = timeArray
        // console.log(state.rsslineOpition.series)
        // const that = this
        // setTimeout(function () {
        //   that.RSSLineChart.setOption({
        //     xAxis:{
        //       type: 'category',
        //       boundaryGap: false,
        //       data: timeArray,
        //       show:false
        //     },
        //     series:state.rsslineOpition.series
        //   },true)
        // },100)
        this.RSSLineChart.setOption(state.rsslineOpition,true,100)
      }
    },
    randArray(len) {
      return Array.from({length:len},  function (){
              return Math.floor(Math.random()*(200))
          }
      );
    },
    refreshRssline(){
      state.rss={}
      this.timeArray=[]
      state.rsslineOpition.xAxis.data=[]
      this.RSSLineChart.setOption(state.rsslineOpition,10)
    },
    replayChart(index){
      if(state.rssLine[state.gatewayChoose][0].length>index[1]-1){

        for(let i=0;i<16;i++){
          state.rsslineOpition.series[i]={
            name: 'RSS'+String(i+1),
            type: 'line',
            symbol: 'none',
            data: state.rssLine[state.gatewayChoose][i].slice(index[0],index[1])
          }
        }
        this.timeArray = this.randArray(index[1]-index[0])
        state.rsslineOpition.xAxis.data=this.timeArray
        this.RSSLineChart.setOption(state.rsslineOpition,10)
      }
    },
  }
}
</script>

<style scoped>
.panels{
  position: relative;
  min-height: 250px;
  height: auto !important;
  aspect-ratio:2.15/1;
  width: 100%;
  border: 1px solid #999999;
  background-color: rgba(153,153,153,0.17);
}
.panels::before{
  position: absolute;
  top: 0;
  left: 0;
  width: 20px;
  height: 20px;
  border-left: 3px solid white;
  border-top: 3px solid white;
  content: "";
  z-index: 99;
}
.panels::after{
  position: absolute;
  top: 0;
  right: 0;
  width: 20px;
  height: 20px;
  border-right: 3px solid white;
  border-top: 3px solid white;
  content: "";
}
.panels-foot{
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
}
.panels-foot::before{
  position: absolute;
  bottom: 0;
  left: 0;
  width: 20px;
  height: 20px;
  border-left: 3px solid white;
  border-bottom: 3px solid white;
  content: "";
}
.panels-foot::after{
  position: absolute;
  bottom: 0;
  right: 0;
  width: 20px;
  height: 20px;
  border-right: 3px solid white;
  border-bottom: 3px solid white;
  content: "";
}
</style>
