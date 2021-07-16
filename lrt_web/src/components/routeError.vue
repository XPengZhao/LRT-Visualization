<template>
  <div class="panels">
    <div style="width:100%;height:100%" ref="routerrorchart"></div>
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
export default {
  name: "Route",
  methods: {
    initRouteErrorCharts() {
      this.routeErrorChart = echarts.init(this.$refs.routerrorchart, 'dark');
      this.routeErrorChart.setOption(state.routeErrorOpition)
      window.addEventListener("resize", () => {
        this.routeErrorChart.resize()
      })
    },
    updateChart(){
      for(let key in state.groundTruth){
        state.routeErrorOpition.series.push({
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
      state.routeErrorOpition.series[1].data = state.roundp
      state.routeErrorOpition.series[2].data = state.roundr1
      state.routeErrorOpition.series[0].data = state.truthError
      this.routeErrorChart.setOption(state.routeErrorOpition,10)
      // const that = this
      // setTimeout(function (){
      //   console.log(111)
      //   that.routeErrorChart.setOption({
      //     series:state.routeErrorOpition.series
      //   })
      // },10)
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
  width: 80%;
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
