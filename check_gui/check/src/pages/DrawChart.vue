<template>
  <nav class="navbar navbar-expand-lg" style="background-color: #04254E; z-index: 999">
    <a class="navbar-brand" href="#"  style=" color: white;">
<!--      <img :src="flowerimg" style="height: 30px">-->
      EPC Space
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <div class="dropdown">
          <button class="btn" style="background-color: #04254E;color: white;min-width: 160px" type="button" v-on:click="uploader_online()" id="connectBtn">
            <img :src="connectimg" style="height: 20px;">
            Connect
          </button>
          <button class="btn" style="background-color: #04254E;color: white;min-width: 160px" type="button" v-on:click="stopConnect()" id="stopBtn">
            <img :src="stopimg" style="height: 20px;">
            Stop
          </button>
        </div>
      </div>
    </div>
  </nav>
<!--  <input type="file" v-on:change="uploader($event)" webkitdirectory directory v-show="false" id="uparea"/>-->
  <div class="mainBox row mt-5">
    <div  class="col-6" style="width: 100%">
      <div class="panels">
        <div ref="checkdiv" style="height: 1100px; width: 100%;position: relative"></div>
        <div class="panels-foot"></div>
      </div>
    </div>
    <div id="checkTable" class="col-6" style="height: 1100px;width: 100%">
      <div class="panels" style="background-color: #100C2A">
          <ag-grid-vue style="width: 100%; height: 600px;background-color: white"
                       ref="table"
                       class="ag-theme-alpine"
                       :gridOptions="gridOptions"
                       @grid-ready="onGridReady"
                       :defaultColDef="defaultColDef"
                       :columnDefs="columnDefs"
                       :rowData="tableData">
          </ag-grid-vue>
        <div class="panels-foot"></div>
      </div>
      <div class="row" style="position: absolute">
        <div class="panels ml-3" style="background-color: #100C2A;height: 500px; width: 650px">
          <div class="mt-5" style="color: #b4a5a5;height: 100%;">
            <h5  class="ml-5">Total Tags: {{getTags()}}</h5>
            <h5  class="ml-5">Total Time: {{getTimes()}}</h5>
          </div>
          <div class="panels-foot"></div>
        </div>
      </div>

    </div>

  </div>
</template>

<script>
/* eslint-disable */
import stomp from 'stompjs'
import { state } from '@/store/state'
import * as echarts from 'echarts/core';
import {compSpectrum,convPhase} from '../public/spectrum'
import {AgGridVue} from 'ag-grid-vue3'
import { HeatmapChart } from 'echarts/charts';
import { Scatter3DChart } from 'echarts-gl/charts';
import { Grid3DComponent } from 'echarts-gl/components';
import { GridComponent,TooltipComponent} from 'echarts/components';
import { VisualMapComponent,AxisPointerComponent,LegendComponent,TitleComponent,ToolboxComponent,DataZoomComponent,CalendarComponent,TimelineComponent } from 'echarts/components';
import parse from 'fast-json-parse'
echarts.use([TooltipComponent,HeatmapChart,GridComponent,Scatter3DChart,ToolboxComponent,DataZoomComponent,TimelineComponent,Grid3DComponent,VisualMapComponent,AxisPointerComponent,LegendComponent,CalendarComponent,TitleComponent]);
export default {
  name: "DrawChart",
  data() {
    return {
      phaseData:Array(8),
      connectimg: require('@/assets/connect.png'),
      checkData:{},
      AllTimes:0,
      checkTable:null,
      columnDefs:[],
      rowData:[],
      tableData:[],
      defaultColDef:{},
      gridOptions:{},
      stopimg:require('@/assets/stop.png'),
    }
  },
  beforeMount() {
    this.columnDefs = [
      {field:'id'},
      {field:'EPC'},
      {field: 'Times'},
      {field: 'Timestamp'},
      {field: 'Rss'},
    ]
    this.defaultColDef={
      sortable: true, //开启排序
      resizable: true,//是否可以调整列大小，就是拖动改变列大小
      filter: true,  //开启刷
    }
    this.gridOptions={
      pagination: true,  //开启分页（前端分页）
      paginationAutoPageSize: true,
    }
  },
  mounted() {
    this.initCheckChart()
    this.phaseData.fill(0)
    $('#stopBtn').prop('disabled',true)
  },
  components:{
    AgGridVue
  },
  methods: {
    onGridReady(){
      this.gridOptions.api.sizeColumnsToFit();
      // this.gridOptions.columnApi.autoSizeAllColumns();
    },
    getTags(){
      return Object.keys(this.checkData).length
    },
    getTimes(){
      return this.AllTimes
    },
    initCheckChart() {
      this.checkChart = echarts.init(this.$refs.checkdiv, 'dark')
      this.checkChart.setOption(state.checkOpition)
      window.addEventListener("resize", () => {
        this.checkChart.resize()
      })
    },
    updateCheckChart(){
      let mid = []
      if(this.checkData){
        for(let key in this.checkData){
          mid.push(this.checkData[key])
        }
        state.checkOpition.series[0].data=mid
      }
      this.checkChart.setOption(state.checkOpition)
    },
    updateCheckTable(){
      this.tableData=[]
      if(this.rowData){
        for(let key in this.rowData){
          this.tableData.push(this.rowData[key])
        }
      }
    },
    uploader_online(){
      $('#connectBtn').prop('disabled',true)
      $('#stopBtn').prop('disabled',false)
      const API = localStorage.getItem('ApiUrl')
      this.ws = new WebSocket(API)
      // this.ws = new WebSocket('ws://158.132.255.178:15674/ws')
      // this.ws = new WebSocket('ws://127.0.0.1:15674/ws')
      this.client = stomp.over(this.ws)
      this.client.heartbeat.incoming = 0
      this.client.heartbeat.outgoing = 1000
      this.client.connect('admin','admin',this.onconnect,this.disconnect,'/')
    },
    disconnect(){
      console.log('Communication has stopped.')
    },
    onconnect(){
      const that = this
      that.InventorySubclient = that.client.subscribe('/queue/Inventory',function (data){
        that.AllTimes++
        let word = data.body
        let loadData = parse(word).value
        for(let key in loadData){
          if(that.checkData[key]){
            that.checkData[key][3] += loadData[key].times
            let date = new Date(loadData[key].timestamp*1000)
            that.rowData[key].Timestamp=date.toLocaleString()
            that.rowData[key].Times += loadData[key].times
          }else {
            let len = that.getTags()+1
            that.checkData[key] = loadData[key].pos
            let date = new Date(loadData[key].timestamp*1000)
            that.rowData[key]={
              id:len,
              EPC:key.toUpperCase(),
              Times:loadData[key].times,
              Timestamp:date.toLocaleString(),
              Rss:loadData[key].rss
            }
            that.checkData[key].push(loadData[key].times)
          }
        }
        that.updateCheckChart()
        state.checkOpition.series[1].data = []
        that.updateCheckTable()
        })
      that.CommandInventorySubclient = that.client.subscribe('/queue/Command_Inventory',function (data) {
        var setData = []
        let word = data.body
        let loadData = parse(word).value
        for (let key in loadData){
          let mid = loadData[key].pos
          mid.push(0.01)
          setData.push(mid)
        }
        state.checkOpition.series[1].data = setData

      })
      that.PhaseSubclient = that.client.subscribe('/queue/Phase',function (data) {
        let word = data.body
        let loadData = parse(word).value
        that.phaseData = convPhase(loadData.phase0,loadData.phaseA,loadData.phaseB)
      })

    },
    stopConnect(){
      $('#connectBtn').prop('disabled',false)
      $('#stopBtn').prop('disabled',true)
      if(this.InventorySubclient){
        this.InventorySubclient.unsubscribe()
      }
      if (this.ws){
        this.ws.close()
      }
    },
  },
}
</script>

<style scoped>
@import "../../node_modules/ag-grid-community/dist/styles/ag-grid.css";
@import "../../node_modules/ag-grid-community/dist/styles/ag-theme-alpine.css";
.mainBox{
  margin: 0 auto;
  height: 1100px;
  width: 100%;
  position:relative;
  z-index:5;
  top:0;
}
.panels{
  position: relative;
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
