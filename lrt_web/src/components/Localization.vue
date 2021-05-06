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
    tagList: []

  }
  },
  methods:{
    initLocalizationCharts () {
      this.LocalizationChart = echarts.init(this.$refs.localizationchart,'dark');
      this.LocalizationChart.setOption(state.localOpition)
      window.addEventListener("resize",()=>{
        this.LocalizationChart.resize()
      })
    },
    upDateLocalization(data,tag){
      let posData = []
      if(tag in this.tagList){
        this.pos[tag].push(data)
      }else{
        this.pos[tag] = [data]
        this.tagList.push('Tag'+tag)
      }
      for(let i in this.pos){
        if(this.pos[i].length>1)
          this.pos[i].shift()
      }
      for(let i in this.pos){
        posData.push({
          name:'Tag'+i,
          type: 'effectScatter',
          symbolSize: 20,
          data: this.pos[i]
        })

      }

      state.localOpition.series=posData
      state.localOpition.legend.data = this.tagList
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
  aspect-ratio:1/1;
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
