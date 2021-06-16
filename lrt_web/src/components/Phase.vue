<template>
  <div class="panels mr-3">
    <div style="width:100%;height:100%" ref="phasechart"></div>
    <div class="panels-foot"></div>
  </div>
</template>

<script>
let echarts = require("echarts/lib/echarts");
import { state } from '@/store/state'
require('echarts/lib/chart/line')
require('echarts/lib/component/title')
require('echarts/lib/component/toolbox')
require('echarts/lib/component/tooltip')
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
  name: "Phase",
  data(){
    return{
      selected : Array(),
      timeArray:[],
    }
  },
  methods: {
    initPhaseCharts() {
      this.PhaseChart = echarts.init(this.$refs.phasechart, 'dark')
      this.PhaseChart.setOption(state.phaseOpition);
      window.addEventListener("resize", () => {
        this.PhaseChart.resize()
      })

    },
    upDatePhase(){
      if(state.phase[state.gatewayChoose]){

        for(let key in state.phase){
          if(state.phase[key][0].length>200){
            for(let i=0;i<16;i++){
              state.phase[key][i].shift()
            }
          }
        }
        let timeArray = this.randArray(state.phase[state.gatewayChoose].length)
        for(let i=0;i<16;i++){
          if(state.antselect[i]){
            state.phaseOpition.series[i]={
              name: 'ANT'+String(i+1),
              type: 'line',
              symbol: 'none',
              // stack: 'phase',
              data: state.phase[state.gatewayChoose][i]
            }
          }else {
            state.phaseOpition.series[i]={
              name: 'ANT'+String(i+1),
              type: 'line',
              symbol: 'none',
              // stack: 'phase',
              data: []
            }
          }
        }
        state.phaseOpition.xAxis.data=timeArray
        this.PhaseChart.setOption(state.phaseOpition,true,10)
      }
    },
    refreshChart(){
      this.timeArray=[]
      state.phase={}
      state.phaseOpition.xAxis.data=[]
      state.antselect=[false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]
      this.PhaseChart.setOption(state.phaseOpition,10)
    },
    replayChart(index){
      if(state.phase[state.gatewayChoose][0].length>index[1]-1){
        for(let i=0;i<16;i++){
          state.phaseOpition.series[i]={
            name: 'ANT'+String(i+1),
            type: 'line',
            symbol: 'none',
            // stack: 'phase',
            data: state.phase[state.gatewayChoose][i].slice(index[0],index[1])
          }
        }

        this.timeArray = this.randArray(index[1]-index[0])
        state.phaseOpition.xAxis.data=this.timeArray
        this.PhaseChart.setOption(state.phaseOpition,10)
      }

    },

    randArray(len) {
      return Array.from({length:len},  function (){
        return Math.floor(Math.random()*(len))
      })
    },
  }
}
</script>

<style scoped>
.panels{
  position: relative;
  min-height: 250px;
  height: auto !important;
  aspect-ratio:2.1/1;
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
