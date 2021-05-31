<template>
  <div class="localization">
    <div style="width:100%;height:100%" ref="localizationchart"></div>
    <div class="localization-foot"></div>
  </div>
</template>

<script>
let echarts = require("echarts/lib/echarts");
require('echarts/lib/chart/scatter')
require('echarts/lib/component/title')
require('echarts/lib/component/toolbox')
require('echarts/lib/component/tooltip')
import { state } from '@/store/state'
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
import { GraphChart } from 'echarts/charts';
echarts.use([GraphChart]);
export default {

name: "Localization",
  data(){
  return{
    pos:[],
    tagList: [],
    pic:state.atnPic,
    star:state.starImg
  }
  },
  methods:{
    initLocalizationCharts () {
      this.LocalizationChart = echarts.init(this.$refs.localizationchart,'dark');
      this.LocalizationChart.setOption(state.localOpition)
      window.addEventListener("resize",()=>{
        this.LocalizationChart.resize()
      })
      this.LocalizationChart.on('click',function (params){
        state.gatewayChoose = params.seriesName
      })
    },
    upDateLocalization(data,tag,truth,xRange,yRange){
      let posData = []
      if(tag in this.tagList){
        this.pos[tag].push(data)
      }else{
        this.pos[tag] = [data]
        this.tagList.push('Tag'+tag)
      }
      for(let i in this.pos){
        if(this.pos[i].length>100)
          this.pos[i].shift()
      }
      // console.log(this.pos)
      for(let i in this.pos){
        posData.push({
          name: i,
          type: 'scatter',
          symbolSize:10,
          data: this.pos[i]
        })
        posData.push({
          name:'Tag'+i,
          type: 'effectScatter',
          data: [data],
          symbolSize:30,
        })

      }
      for(let key in state.atnpos){
        posData.push({
          name:key,
          type: 'scatter',
          data: [[state.atnpos[key][0],state.atnpos[key][2]]],
          symbol: this.pic,
          itemStyle:{
            color: 'white'
          },
          symbolSize:[35,50],
          showAllSymbol:true,
        })
      }
      posData.push({
        name:'Truth',
        type: 'scatter',
        data: [[truth[0],truth[2]]],
        symbol: this.star,
        itemStyle:{
          color: 'yellow'
        },
        symbolSize:[20,20],
        showAllSymbol:true,
      })
      state.localOpition.series=posData
      state.localOpition.xAxis.min = xRange[0]*2
      state.localOpition.xAxis.max = xRange[1]*2
      state.localOpition.yAxis.min = yRange[0]*2
      state.localOpition.yAxis.max = yRange[1]*2
      state.localOpition.legend.data = this.tagList
      this.LocalizationChart.setOption(state.localOpition,500)
    },
    refreshChart(){
      state.localOpition.series=[]
      state.localOpition.legend.data = []
      this.pos = []
      this.tagList = []
      this.LocalizationChart.setOption(state.localOpition,500)
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
