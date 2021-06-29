<template>
  <div class="panels">
    <div style="width:100%;height:100%" ref="confidenceBarchart"></div>
    <div class="panels-foot"></div>
  </div>
</template>

<script>
import {state} from "@/store/state";
import {BarChart, EffectScatterChart} from 'echarts/charts';
import {CalendarComponent, GridComponent, LegendComponent, TimelineComponent} from 'echarts/components'

let echarts = require("echarts/lib/echarts");
require('echarts/lib/component/title')
require('echarts/lib/component/toolbox')
require('echarts/lib/component/tooltip')
require('echarts/lib/component/dataZoom')
echarts.use([BarChart]);
echarts.use([GridComponent])
echarts.use([LegendComponent]);
echarts.use([CalendarComponent]);
echarts.use([EffectScatterChart]);
echarts.use([TimelineComponent]);

export default {
  name: "errorBar",
  data(){
    return{
      errorBarDataArr:[],
    }
  },
  methods: {
    initErrorBarCharts() {
      this.confidenceBarChart = echarts.init(this.$refs.confidenceBarchart, 'dark');
      this.confidenceBarChart.setOption(state.confidenceBarOpition)
      window.addEventListener("resize", () => {
        this.confidenceBarChart.resize()
      })
    },
    compBar(){
      let data = []
      for (let key in state.confidence){
        if(key!=='0'){
          data.push(state.confidence[key].length)
        }
      }
      return data
    },
    compLine(){
      let data = this.compBar()
      let wholeData = data[0]+data[1]+data[2]
      return [parseInt((data[0]/wholeData)*100),parseInt((data[1]/wholeData)*100),parseInt((data[2]/wholeData)*100)]
    },
    updateChart(){
      state.confidenceBarOpition.series[0].data = this.compBar()
      state.confidenceBarOpition.series[1].data = this.compLine()
      this.confidenceBarChart.setOption(state.confidenceBarOpition)
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
