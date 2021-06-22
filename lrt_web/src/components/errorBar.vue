<template>
  <div class="panels mr-3">
    <div style="width:100%;height:100%" ref="errorbarchart"></div>
    <div class="panels-foot"></div>
  </div>
</template>

<script>
import {state} from "@/store/state";
let echarts = require("echarts/lib/echarts");
require('echarts/lib/chart/scatter')
require('echarts/lib/component/title')
require('echarts/lib/component/toolbox')
require('echarts/lib/component/tooltip')
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
  name: "errorBar",
  data(){
    return{
      errorBarDataArr:[],
    }
  },
  methods: {
    initErrorBarCharts() {
      this.errorBarChart = echarts.init(this.$refs.errorbarchart, 'dark');
      this.errorBarChart.setOption(state.errorBarOpition)
      window.addEventListener("resize", () => {
        this.errorBarChart.resize()
      })
    },
    updateChart(){
      console.log(state.truthArray)
      state.errorBarOpition.series[0].data = state.truthArray
      this.errorBarChart.setOption(state.errorBarOpition)
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
