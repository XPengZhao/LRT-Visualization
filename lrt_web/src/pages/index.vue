<template>
  <div class="mainBox">
    <div ref="topology" style="min-height: 800px;margin: 30px;top:100px"></div>
  </div>
</template>

<script>
import {state} from "@/store/state";
import * as echarts from 'echarts';
import {useRouter} from "vue-router"
import stomp from "stompjs";
/* eslint-disable */
export default {
  name: "index",
  mounted() {
    this.initTopology()
    this.init()

    this.uploader_online()
  },
  data(){
      return{
        databaseImg:'image://'+require('@/assets/database.png'),
        serverImg:'image://'+require('@/assets/server.png'),
        guiImg:"image://"+require('@/assets/gui.png'),
        gatewayImg:"image://"+require('@/assets/gateway.png'),
        optitrackImg:"image://"+require('@/assets/optitrack.png'),
        gateway1:true,
        gateway2:true,
        gateway3:true,
        optitrack:true

      }
  },
  methods: {
    init(){
      const that = this
      this.loop = setInterval(function () {
        that.Topology.setOption(state.topologyOpition,100)
      },30000)
    },
    initTopology(){
      const that = this
        const router = useRouter()
        this.Topology = echarts.init(this.$refs.topology)
      state.topologyOpition.series[0].data=[
        {
          name: 'Database',
          x: 50,
          y: 30,
          symbol: this.databaseImg,
          symbolSize:[100,100],
          showAllSymbol:true,

        },{
          name: 'Database Server',
          x: 200,
          y: 30,
          symbol: this.serverImg,
          symbolSize:[100,100],
          showAllSymbol:true,

        },{
          name: 'GUI',
          x: 400,
          y: 30,
          symbol: this.guiImg,
          symbolSize:[100,100],
          showAllSymbol:true,

        }, {
          name: 'X Server',
          x: 300,
          y: 200,
          symbol: this.serverImg,
          symbolSize:[100,100],
          showAllSymbol:true,
        },
        {
          name: 'Gateway',
          x: -50,
          y: 500,
          symbol: this.serverImg,
          symbolSize:[0,0],
          showAllSymbol:false,
        },
        ]
      state.topologyOpition.series[0].links = [
        {
          source: 'GUI',
          target: 'X Server',
          lineStyle: {
            opacity: 1,
            width: 5,
            curveness: 0.5,
            color:'#007580',
          }
        },{
          source: 'Database',
          target: 'Database Server',
          lineStyle: {
            opacity: 1,
            width: 5,
            curveness: 0,
            color:'#007580',
          }
        },{
          source: 'GUI',
          target: 'Database Server',
          lineStyle: {
            opacity: 1,
            width: 5,
            curveness: 0,
            color:'#007580',
          }
        }
      ]
        this.Topology.setOption(state.topologyOpition)
        window.addEventListener("resize",()=>{
          this.Topology.resize()
        })
      this.Topology.on('click',function (params){
            let self = this
            self.nodeIdx = params.dataIndex
        console.log(self.nodeIdx)
            if(self.nodeIdx===2){
              state.queue = 'oss.url_test'
              that.stopConnect()
              router.push({
                name: 'Show'
              })
            }
            if(self.nodeIdx===0){
              that.stopConnect()
              router.push({
                name: 'dataList'
              })
            }
          })
      },
    uploader_online(){
      $('#stopButton').prop('disabled',false)
      $('#onlineButton').addClass('disabled')
      $('#recordButton').prop('disabled',false)
      const ws = new WebSocket(localStorage.getItem("MQUrl"))
      this.client = stomp.over(ws)
      this.client.heartbeat.incoming = 0
      this.client.heartbeat.outgoing = 10000
      // this.client.connect('admin','admin',this.onconnect,this.disconnect,'/')
      this.client.connect('admin','admin',this.onconnect,this.disconnect,'/')

    },
    disconnect(e){
      // this.uploader_online()
      console.log(e)
      // console.log('Reconnect')
    },
    onconnect(){
      const that = this
      this.gateway1Subclient = this.client.subscribe('/queue/Gateway1',function (data) {
        if(that.gateway1){
          state.topologyOpition.series[0].data.push({
            name: 'Gateway1',
            x: 100,
            y: 500,
            symbol: that.gatewayImg,
            symbolSize:[100,100],
            showAllSymbol:true,
          })
          state.topologyOpition.series[0].links.push(
              {
                source: 'X Server',
                target: 'Gateway1',
                lineStyle: {
                  opacity: 1,
                  width: 5,
                  curveness: -0.5,
                  color:'#007580',
                }
              },
          )
          that.gateway1=false
          if(that.gateway1Timeout){
            clearTimeout(that.gateway1Timeout)
          }
          that.gateway1Timeout = setTimeout(function (){
                state.topologyOpition.series[0].data.splice(state.topologyOpition.series[0].data.findIndex(item=>item.name==='Gateway1'),1)
                state.topologyOpition.series[0].links.splice(state.topologyOpition.series[0].links.findIndex(item=>item.target==='Gateway1'),1)
                that.gateway1=true
              }
          ,15000)
        }

            that.Topology.setOption(state.topologyOpition,100)
      },{durable:true,'auto-delete':false,'x-message-ttl':5000,'message-ttl':1000})

      this.gateway2Subclient = this.client.subscribe('/queue/Gateway2',function (data) {
        if(that.gateway2){
          state.topologyOpition.series[0].data.push({
            name: 'Gateway2',
            x: 200,
            y: 500,
            symbol: that.gatewayImg,
            symbolSize:[100,100],
            showAllSymbol:true,
          })
          state.topologyOpition.series[0].links.push(
              {
                source: 'X Server',
                target: 'Gateway2',
                lineStyle: {
                  opacity: 1,
                  width: 5,
                  curveness: -0.5,
                  color:'#007580',
                }
              },
          )
          that.gateway2=false
          if(that.gateway2Timeout){
            clearTimeout(that.gateway2Timeout)
          }
          that.gateway2Timeout = setTimeout(function (){
                state.topologyOpition.series[0].data.splice(state.topologyOpition.series[0].data.findIndex(item=>item.name==='Gateway2'),1)
                state.topologyOpition.series[0].links.splice(state.topologyOpition.series[0].links.findIndex(item=>item.target==='Gateway2'),1)
                that.gateway2=true
              }
              ,15000)
        }

        that.Topology.setOption(state.topologyOpition,100)
      },{durable:true,'auto-delete':false,'x-message-ttl':5000,'message-ttl':1000})

      this.gateway3Subclient = this.client.subscribe('/queue/Gateway3',function (data) {
        if(that.gateway3){
          state.topologyOpition.series[0].data.push({
            name: 'Gateway3',
            x: 400,
            y: 500,
            symbol: that.gatewayImg,
            symbolSize:[100,100],
            showAllSymbol:true,
          })
          state.topologyOpition.series[0].links.push(
              {
                source: 'X Server',
                target: 'Gateway3',
                lineStyle: {
                  opacity: 1,
                  width: 5,
                  curveness: -0.5,
                  color:'#007580',
                }
              },
          )
          that.gateway3=false
          if(that.gateway3Timeout){
            clearTimeout(that.gateway3Timeout)
          }
          that.gateway3Timeout = setTimeout(function (){
                state.topologyOpition.series[0].data.splice(state.topologyOpition.series[0].data.findIndex(item=>item.name==='Gateway3'),1)
                state.topologyOpition.series[0].links.splice(state.topologyOpition.series[0].links.findIndex(item=>item.target==='Gateway3'),1)
                that.gateway3=true
              }
              ,15000)
        }
        that.Topology.setOption(state.topologyOpition,100)
      },{durable:true,'auto-delete':false,'x-message-ttl':5000,'message-ttl':1000})

      this.optitrackSubclient = this.client.subscribe('/queue/Optitrack',function (data) {
        if(that.optitrack){
          state.topologyOpition.series[0].data.push({
            name: 'Optitrack',
            x: 400,
            y: 500,
            symbol: that.gatewayImg,
            symbolSize:[100,100],
            showAllSymbol:true,
          })
          state.topologyOpition.series[0].links.push(
              {
                source: 'X Server',
                target: 'Optitrack',
                lineStyle: {
                  opacity: 1,
                  width: 5,
                  curveness: -0.5,
                  color:'#007580',
                }
              },
          )
          that.optitrack=false
          if(that.optitrackTimeout){
            clearTimeout(that.optitrackTimeout)
          }
          that.optitrackTimeout = setTimeout(function (){
                state.topologyOpition.series[0].data.splice(state.topologyOpition.series[0].data.findIndex(item=>item.name==='Optitrack'),1)
                state.topologyOpition.series[0].links.splice(state.topologyOpition.series[0].links.findIndex(item=>item.target==='Optitrack'),1)
                that.optitrack=true
              }
              ,15000)
        }
        that.Topology.setOption(state.topologyOpition,100)
      },{durable:true,'auto-delete':false,'x-message-ttl':5000,'message-ttl':1000})
    },
    stopConnect(){
      clearInterval(this.loop)
      this.gateway1Subclient.unsubscribe()
      this.gateway2Subclient.unsubscribe()
      this.gateway3Subclient.unsubscribe()
      this.optitrackSubclient.unsubscribe()
      this.client.disconnect()
    },
  }
}
</script>

<style scoped>
.mainBox{
  margin: 0 auto;
  top: 70px;
  min-height: 1100px;
  width: 80%;
  position:relative;
  z-index:5;
  border-radius: 20px;
  /*background-color: #d8ebe4;*/
  background-color: #dddddd;
}

</style>
