<template>
  <div class="card panels" style="background-color: #100C2A" >
      <div class="card-body" style="top:-5%">
        <div style="width: 100%;height: auto;aspect-ratio:1/1;" ref="rsscharts"></div>
      </div>
    <div class="panels-foot"></div>
  </div>
</template>

<script>
let echarts = require("echarts/lib/echarts");
require("echarts/lib/chart/heatmap")
require('echarts/lib/component/title')
require('echarts/lib/component/toolbox')
require('echarts/lib/component/tooltip')
require('echarts/lib/component/visualMap')
import {state} from "@/store/state";
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
import { GaugeChart } from 'echarts/charts';
echarts.use([GaugeChart]);
export default {
name: "RSS",
  data(){
  return{
    rssx : [0,1,2,3],
    rssy : [0,1,2,3],
    // RSSChart:[]
  }
  },
  methods:{
    initRSSCharts () {
      this.RSSChart = echarts.init(this.$refs.rsscharts,'dark')
      this.RSSChart.setOption(state.rssOpition)
      window.addEventListener("resize",()=>{
        this.RSSChart.resize()
      })
      },

    upDateRSS(){
      // state.rssOpition.animation=false
      if(state.rss[state.gatewayChoose]) {
        for (let i = 0; i < 16; i++) {
          state.rssOpition.series[i].data = [state.rss[state.gatewayChoose][i]]
        }
        this.RSSChart.setOption(state.rssOpition,true, 150)
      }
    },
    refreshCharts(){
      for(let i=0;i<16;i++) {
        state.rssOpition.series[i].data = [-70]
      }
      state.rss={}
      this.RSSChart.setOption(state.rssOpition,150)
    },
    replayChart(index){
      if(state.rss[state.gatewayChoose][index]){
        for (let i = 0; i < 16; i++) {
          state.rssOpition.series[i].data = [state.rss[state.gatewayChoose][index][i]]
        }
      }else {
        for (let i = 0; i < 16; i++) {
          state.rssOpition.series[i].data = [-50]
        }
      }

      this.RSSChart.setOption(state.rssOpition,true, 150)
    }

  }
}
</script>

<style scoped>
.panels{
  position: relative;
  min-height: 250px;
  height: auto !important;
  width: 100%;
  border: 1px solid #999999;
  /*background-color: rgba(153,153,153,0.17);*/
  background-color: pink;
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
