<template>
  <div class="panels mr-3">
    <div style="width:100%;height:100%" ref="confidenceCdfchart"></div>
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
require('echarts/lib/component/dataZoom')
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
  name: "errorLine",
  data(){
    return{
      selected : Array(),
      timeArray:[],
      errorArray:[],
    }
  },
  methods: {
    initConfidenceCdfCharts() {
      this.confidenceCdfChart = echarts.init(this.$refs.confidenceCdfchart, 'dark');
      this.confidenceCdfChart.setOption(state.confidenceCdfOpition)
      window.addEventListener("resize", () => {
        this.confidenceCdfChart.resize()
      })
    },
    updateCharts(cdf){
      for(let key in cdf){
        let yData = cdf[key].ps()
        let xData = cdf[key].xs()
        let posData = yData.map(function (num,index){
          return [xData[index],num]
        })
        state.confidenceCdfOpition.series.push({
              name: "Confidence "+key,
              data: posData,
              type: 'line',
            smooth: true
        })
        state.confidenceCdfOpition.series.push({
          type: 'scatter',
          symbolSize:20,
          data: [posData[state.ccdfIndex[key][0]]]
        })

        state.confidenceCdfOpition.legend.data.push('Confidence '+key)
      }
      this.confidenceCdfChart.setOption(state.confidenceCdfOpition,true,100)
    },
  }
}
</script>

<style scoped>
.panels{
  z-index: 20;
  position: relative;
  min-height: 250px;
  height: auto !important;
  aspect-ratio:1.5/1;
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