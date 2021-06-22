<template>
  <div class="panels mr-3">
    <div style="width:100%;height:100%" ref="routechart"></div>
    <div class="panels-foot"></div>
  </div>
</template>

<script>
import {state} from "../store/state";
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
import { PieChart } from 'echarts/charts';
echarts.use([PieChart]);
export default {
  name: "Route",
  methods: {
    initRouteCharts() {
      this.routeChart = echarts.init(this.$refs.routechart, 'dark');
      this.routeChart.setOption(state.routeOpition)
      window.addEventListener("resize", () => {
        this.routeChart.resize()
      })
    },
    updateChart(){
      for(let key in state.groundTruth){
        state.routeOpition.series.push({
          name:key,
          type: 'scatter',
          data: [state.groundTruth[key]],
          symbol: state.atnPic,
          itemStyle: {
            color: 'white'
          },
          symbolSize: [15,15],
          showAllSymbol: true,
        })
      }
      state.routeOpition.series[1].data = state.roundp
      state.routeOpition.series[2].data = state.roundr1
      state.routeOpition.series[0].data = state.truthConfidence
      this.routeChart.setOption(state.routeOpition,10)
    }

  }
}
</script>

<style scoped>
.panels{
  position: relative;
  min-height: 250px;
  height: auto !important;
  aspect-ratio:1/1;
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
