<template>
  <div class="card panels" style="background-color: #100C2A" >
      <div class="card-body" style="top:-5%">
        <div style="width: 100%;height: auto;aspect-ratio:1/1;" ref="rsscharts"></div>
<!--        <div class="row">-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart1"></div>-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart2"></div>-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart3"></div>-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart4"></div>-->
<!--        </div>-->
<!--        <div class="row">-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart5"></div>-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart6"></div>-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart7"></div>-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart8"></div>-->
<!--        </div>-->
<!--        <div class="row">-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart9"></div>-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart10"></div>-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart11"></div>-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart12"></div>-->
<!--        </div>-->
<!--        <div class="row">-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart13"></div>-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart14"></div>-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart15"></div>-->
<!--          <div style="width: 24%;height: auto;aspect-ratio:1/1;" ref="rsschart16"></div>-->
<!--        </div>-->
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
      },

    upDateRSS(data){
      // state.rssOpition.animation=false
      for(let i=0;i<16;i++) {
        state.rssOpition.series[i].data = [data[i]]
      }
        this.RSSChart.setOption(state.rssOpition,100)
    },
    refreshCharts(){
      for(let i=0;i<16;i++) {
        state.rssOpition.series[i].data = [-70]
      }
      this.RSSChart.setOption(state.rssOpition,100)
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
