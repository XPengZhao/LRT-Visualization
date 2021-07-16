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
require('echarts/lib/component/dataZoomInside')
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
import { LineChart } from 'echarts/charts';
echarts.use([LineChart]);
import { VisualMapComponent } from 'echarts/components';
echarts.use([VisualMapComponent]);
export default {

name: "Localization",
  data(){
  return{
    pos:[],
    tagList: [],
    pic:state.atnPic,
    star:state.starImg,
    atnR:5,
    atnRound:[],
    oneMeterRound:[],
    atnPos:{},
    truth:[]
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
    antColor(key){
      return key === state.gatewayChoose?"red":"white"
    },
    upDateLocalization(data,tag,truth,gateway){
      // console.log(gateway)
      let posData = [{
        type: 'line',
        symbol:'none',
        symbolSize:0,
        data: state.oneMeterRound,
        smooth:true,
      },{
        type: 'line',
        symbol:'none',
        symbolSize:0,
        data: state.atnRound,
        smooth:true,
      }]
      // if(tag in this.tagList){
      //   this.pos[tag].push(truth)
      // }else{
      //   this.pos[tag] = [truth]
      //   this.tagList.push('Tag'+tag)
      // }
      this.truth.push(truth)
      if(this.truth.length>10){
        this.truth.shift()
      }
      // for(let i in this.pos){
      //   if(this.pos[i].length>10){
      //     this.pos[i].shift()
      //   }
      //   posData.push({
      //     name: i,
      //     type: 'scatter',
      //     data: this.pos[i],
      //   })
      //   posData.push({
      //     name:'Tag'+i,
      //     type: 'effectScatter',
      //     data: [data],
      //     symbolSize:30,
      //   })
      // }

      // posData.push({
      //   name:'Truth',
      //   type: 'scatter',
      //   data: [truth],
      //   symbol: 'pin',
      //   itemStyle:{
      //     color: 'yellow'
      //   },
      //   symbolSize:[20,20],
      // })
      posData.push({
        name: 'Tag1 Truth',
        type: 'scatter',
        data: this.truth,
      })
      console.log(truth)
      console.log(this.truth)
      posData.push({
        name:'Tag1',
        type: 'effectScatter',
        data: [data],
        symbolSize:30,
      })
      for(let key in state.atnPos){
          posData.push({
            name:key,
            type: 'scatter',
            data: [state.atnPos[key]],
            symbol: this.pic,
            itemStyle:{
              color: this.antColor(key),
            },
            symbolSize:[35,50],
            showAllSymbol:true,
          })
        if(gateway[key]){
          posData.push({
            type: 'line',
            name:key+'connect',
            data: [
              state.atnPos[key],
              data
            ],
            connectNulls:false,
            lineStyle:{
              color:'yellow'
            }
          })
        }else {
          posData.push({
            type: 'line',
            name:key+'connect',
            data: []
          })
        }
      }

      // if(state.localOpition.xAxis.min !== xRange[0]*2){
      //   state.localOpition.xAxis.min = xRange[0]*2
      //   state.localOpition.xAxis.max = xRange[1]*2
      //   state.localOpition.yAxis.min = yRange[0]*2
      //   state.localOpition.yAxis.max = yRange[1]*2
      // }
      state.localOpition.legend.data = this.tagList
      const that = this
      setTimeout(function () {
        that.LocalizationChart.setOption({
          legend:{
            type: 'scroll',
            data: that.tagList,
            orient: 'vertical',
            y: '10%',
            x: 'right',
            selectedMode: false,
          },
          series:posData
        })
      },10)
    },
    refreshChart(){
      state.localOpition.series=[]
      state.localOpition.legend.data = []
      this.pos = []
      this.tagList = []
      this.LocalizationChart.setOption(state.localOpition,10)
    },
    replayChart(index){
      let posData = []
      let data = state.replay.position.slice(index[0],index[1])
      data = data.map(function (val) {
        return [val[0],val[2]]
      })
      posData.push({
        name: "Tag1",
        type: 'scatter',
        symbolSize:10,
        data: data
      })
      let truth = state.replay.truth.slice(index[0],index[1])
      let truthData = truth.map(function (val) {
        return [val[0],val[2]]
      })
      posData.push({
        name:'Truth',
        type: 'line',
        data: truthData,
        symbol: this.star,
        itemStyle:{
          color: 'yellow'
        },

        symbolSize:[5,5],
        showAllSymbol:true,
      })
      state.localOpition.legend.data = ["Tag1"]
      state.localOpition.xAxis.min = state.replay.xRange[0]
      state.localOpition.xAxis.max = state.replay.xRange[1]
      state.localOpition.yAxis.min = state.replay.zRange[0]
      state.localOpition.yAxis.max = state.replay.zRange[1]
      const that = this
      setTimeout(function () {
        that.LocalizationChart.setOption({
          series:posData,
          legend:state.localOpition.legend,
          xAxis:state.localOpition.xAxis,
          yAxis:state.localOpition.yAxis
        },true)
      },10)
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
