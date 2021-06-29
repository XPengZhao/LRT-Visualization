<template>
  <div class="panels mr-3">
    <div style="width:100%;height:100%" ref="cdfchart"></div>
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
  name: "Cdf",
  data(){
    return{
      timeArray:[],
    }
  },
  methods: {
    initCdfCharts() {
      this.cdfChart = echarts.init(this.$refs.cdfchart, 'dark');
      this.cdfChart.setOption(state.cdfOpition)
      window.addEventListener("resize", () => {
        this.cdfChart.resize()
      })
    },
    updateChart(cdf){
      let xData = cdf.xs()
      let yData = cdf.ps()
      let posData = yData.map(function (num,index){
        return [xData[index],num]
      })
      state.cdfOpition.series[0].data = posData
        state.cdfOpition.series.push({
          type: 'scatter',
          symbolSize:20,
          data: [posData[state.cdfIndex[0]]]
        })



      this.cdfChart.setOption(state.cdfOpition)
    }
  }
}
</script>

<style scoped>
.panels{
  position: relative;
  min-height: 250px;
  height: auto !important;
  aspect-ratio:2/0.8;
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
