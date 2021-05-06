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
      rss : [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],],
      timearray:[],
      selected : Array(),
      num:0
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
    upDateRSSline(data){
      for(let i=0;i<16;i++){
        this.rss[i].push(data[i])
      }
      if(this.rss[0].length>200){
        for(let i=0;i<16;i++){
          this.rss[i].shift()
        }
      }
      this.timearray.push(this.num)
      if(this.timearray.length>200){
        this.timearray.shift()
      }
      for(let i=0;i<16;i++){
        if(state.antselect[i]){
          state.rsslineOpition.series[i]={
            name: 'ANT'+String(i+1),
            type: 'line',
            symbol: 'none',
            stack: 'rss',
            data: this.rss[i]
          }
        }else {
          state.rsslineOpition.series[i]={
            name: 'ANT'+String(i+1),
            type: 'line',
            symbol: 'none',
            stack: 'phase',
            data: []
          }
        }
      }
      state.rsslineOpition.xAxis.data=this.timearray
      this.RSSLineChart.setOption(state.rsslineOpition,100)
      this.num ++
    }
  }
}
</script>

<style scoped>
.panels{
  position: relative;
  min-height: 410px;
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
