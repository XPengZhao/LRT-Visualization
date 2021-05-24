<template>
  <div style="background-color: black;width: 100%">
    <div class=" panels" style="width: 100%">
      <div class="radar-body" style="width: 100%">
        <div class="radar" style="width: 100%;height: 100%;"></div>
      </div>
      <div style="height:405px;width:100%"  ref="radarchart"></div>
      <div class="panels-foot"></div>
    </div>
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
import { PolarComponent } from 'echarts/components';
echarts.use([PolarComponent]);
export default {
name: "radar",
  data(){
  return{
  }
  },
  methods:{
    initRadarCharts () {
      this.radarChart = echarts.init(this.$refs.radarchart,'dark');
      this.radarChart.setOption(state.radarOpition);
      window.addEventListener("resize",()=>{
        this.radarChart.resize()
      })
    },
    upDateRadar(){
      state.radarOpition.series[0].data=[state.aoa['gateway1']]
      state.radarOpition.series[1].data=[state.aoa['gateway2']]
      this.radarChart.setOption(state.radarOpition,500)
    },
    refreshChart(){
      state.radarOpition.series[0].data=[]
      state.radarOpition.series[1].data=[]
      state.aoa = {}
      this.radarChart.setOption(state.radarOpition,500)
    },

  }

}
</script>

<style scoped>
.radar-body{
  top: 22.5%;
  left: 0;
  position:absolute;
  display: flex;
  width: 100%;
  height: auto;
  aspect-ratio:1/1;
  /*align-items: center;*/
  /*justify-content: center;*/
}
.radar {
  width: 100%;
  height: auto;
  aspect-ratio:1/1;
  font-size: 37px;
  background:
      linear-gradient(rgba(0,0,0,0),rgba(0,0,0,0));
}
.radar {
  position: relative;
}

.radar::before {
  content: '';
  position: absolute;
  width: 40%;
  height: 40%;
}
.radar::before {
  z-index: 9999;
  background: linear-gradient(
      45deg,
      rgba(0, 0, 0, 0) 50%,
      rgba(0, 192, 0, 1) 100%
  );
  border-radius: 100% 0 0 0;
}
.radar {
  border-radius: 50%;
}
/*.radar {*/
/*  width: calc(8em + 1.5em);*/
/*  height: calc(8em + 1.5em);*/
/*}*/

.radar::before {
  top: 10%;
  left: 10%;
}
.radar::before {
  animation: scanning 5s linear infinite;
  transform-origin: 100% 100%;
}

@keyframes scanning {
  to {
    transform: rotate(360deg);
  }
}

.panels{
  position: relative;
  min-height: 410px;
  width: 100%;
  border: 1px solid #999999;
  background:radial-gradient(circle, rgba(3, 177, 0, 0.5), rgba(3, 177, 0, 0.1),rgba(3, 14, 52, 0.8));
  /*background-color: pink;*/
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
