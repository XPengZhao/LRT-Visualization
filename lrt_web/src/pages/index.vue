<template>
  <div class="mainBox">
    <div id="topology" style="min-height: 800px;margin: 30px;top:100px"></div>
  </div>
</template>

<script>
import {state} from "@/store/state";
import * as echarts from 'echarts';
import {useRouter} from "vue-router";
export default {
  name: "index",
  mounted() {
    this.initTopology()
  },
  methods:{
      initTopology(){
          const router = useRouter()
          this.Topology = echarts.init(document.getElementById('topology'))
          this.Topology.setOption(state.topologyOpition)
        window.addEventListener("resize",()=>{
          this.Topology.resize()
        })
          this.Topology.on('click',function (params){
            let self = this
            self.nodeIdx = params.dataIndex
            console.log(self.nodeIdx)
            if(self.nodeIdx===2){
              router.push({
                name: 'Show'
              })
            }
            if(self.nodeIdx===0){
              router.push({
                name: 'dataList'
              })
            }
          })
        },
  },

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
