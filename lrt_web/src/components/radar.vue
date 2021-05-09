<template>
  <div style="background-color: black">
    <div class=" panels" style="height: 400px">
      <div class="radar-body" style="height: 400px;background-color: #1c7430">
        <div class="radar" style="background-color: pink;width: 100%;height: 100%;"></div>
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
    upDateRadar(data){
      state.radarOpition.series[0].data=data
      this.radarChart.setOption(state.radarOpition,500)
    },
    refreshChart(){
      state.radarOpition.series[0].data=[]
      this.radarChart.setOption(state.radarOpition,500)
    },

  }

}
</script>

<style scoped>
.radar-body{
  top: 22px;
  left: 22px;
  position:absolute;
  display: flex;
  height: 400px;
  /*align-items: center;*/
  /*justify-content: center;*/
}
.radar {
  width: 8em;
  height: 8em;
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
  width: calc(8em / 2);
  height: calc(8em / 2);
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
.radar {
  width: calc(8em + 1.5em);
  height: calc(8em + 1.5em);
}

.radar::before {
  top: calc(1.5em / 2);
  left: calc(1.5em / 2);
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
