<template>
  <div class="localization">
    <div style="width:100%;height:100%" ref="localization3Dchart"></div>
    <div class="localization-foot"></div>
  </div>
</template>

<script>
import { state } from '@/store/state'
import * as echarts from 'echarts/core';
import { HeatmapChart } from 'echarts/charts';
import { Scatter3DChart } from 'echarts-gl/charts';
import { Grid3DComponent } from 'echarts-gl/components';
import { GridComponent,TooltipComponent} from 'echarts/components';
import { VisualMapComponent,AxisPointerComponent,LegendComponent,TitleComponent,ToolboxComponent,DataZoomComponent,CalendarComponent,TimelineComponent } from 'echarts/components';
echarts.use([TooltipComponent,HeatmapChart,GridComponent,Scatter3DChart,ToolboxComponent,DataZoomComponent,TimelineComponent,Grid3DComponent,VisualMapComponent,AxisPointerComponent,LegendComponent,CalendarComponent,TitleComponent]);

export default {

name: "Localization",
  data(){
    return{
        truth:[],
      position:[],
    }
  },
  methods:{
    initLocalizationCharts () {
      this.Localization3DChart = echarts.init(this.$refs.localization3Dchart,'dark');
      this.Localization3DChart.setOption(state.local3dOpition)
      window.addEventListener("resize",()=>{
        this.Localization3DChart.resize()
      })
    },
    upDateLocalization(position,truth){
        this.position.push(truth)
        this.truth.push(position)
      // console.log(position)
      console.log(truth)
      if(this.truth.length>100){
        this.truth.shift()
        this.position.shift()
      }
      const  that =this
      setTimeout(function () {
        that.Localization3DChart.setOption({
          series: [{
            name:'position',
            type: 'scatter3D',
            data: that.position
          },{
            name:'truth',
            type: 'scatter3D',
            data: that.truth
          }
          ]
        })
      },100)

    },
    refreshChart(){

    },
    replayChart(){

    }
  }
}
</script>

<style scoped>
.localization{
  position: relative;
  width: 100%;
  height: auto;
  aspect-ratio:1/0.97;
  border: 1px solid #999999;
  background-color: rgba(153,153,153,0.17);
}
.localization::before{
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
.localization::after{
  position: absolute;
  top: 0;
  right: 0;
  width: 20px;
  height: 20px;
  border-right: 3px solid white;
  border-top: 3px solid white;
  content: "";
}
.localization-foot{
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
}
.localization-foot::before{
  position: absolute;
  bottom: 0;
  left: 0;
  width: 20px;
  height: 20px;
  border-left: 3px solid white;
  border-bottom: 3px solid white;
  content: "";
}
.localization-foot::after{
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
