<template>
  <div style="background-color: black; ">
    <div class="card panels">
      <div class="radar-body">
        <div class="radar"></div>
      </div>
      <div class="card-body" style="top:-5%">
        <div class="radarchart"  ref="radarchart"></div>
      </div>

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
    aoaList : []
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
      for(let key in state.aoa){
        this.aoaList.push({
          coordinateSystem: 'polar',
          name: key,
          data: [[state.aoa[key].azimuth,state.aoa[key].elevation]],
          type:'effectScatter',
          color:'red'
        },)
      }
      state.radarOpition.series = this.aoaList
      this.radarChart.setOption(state.radarOpition,150)
    },
    refreshChart(){
      state.radarOpition.series=[]
      state.aoa = {}
      this.radarChart.setOption(state.radarOpition,150)
    },

  }

}
</script>

<style scoped>
.radar-body{
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
  width: 35%;
  height: 35%;
}
.radar::before {
  background: linear-gradient(
      45deg,
      rgba(0, 192, 0, 1) 0%,
      rgba(0, 0, 0, 0) 50%

  );
  border-radius: 0 0 100% 0;
}
.radar {
  border-radius: 50%;
}
/*.radar {*/
/*  width: calc(8em + 1.5em);*/
/*  height: calc(8em + 1.5em);*/
/*}*/

.radar::before {
  top: 50%;
  left: 50%;
}
.radar::before {
  animation: scanning 5s linear infinite;
  transform-origin: 0 0;
}

@keyframes scanning {
  to {
    transform: rotate(360deg);
  }
}
.radarchart{
  width: 100%;
  height: auto;
  aspect-ratio:1/1;
}
.panels{
  position: relative;
  min-height: 250px;
  /*width: auto;*/
  /*aspect-ratio:1/1;*/
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
