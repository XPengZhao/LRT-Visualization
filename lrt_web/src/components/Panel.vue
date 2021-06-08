<template>
  <div class=" mt-2">
    <div class="card panels" style="background-color: #100C2A" >
      <div class="card-body">
          <img class="channel" :src="pic[1]" @click="changeFrame(1)" alt="">
          <img class="channel" :src="pic[2]" @click="changeFrame(2)" alt="">
          <img class="channel" :src="pic[3]" @click="changeFrame(3)" alt="">
          <img class="channel" :src="pic[4]" @click="changeFrame(4)" alt="">
          <img class="channel" :src="pic[5]" @click="changeFrame(5)" alt="">
          <img class="channel" :src="pic[6]" @click="changeFrame(6)" alt="">
          <img class="channel" :src="pic[7]" @click="changeFrame(7)" alt="">
          <img class="channel" :src="pic[8]" @click="changeFrame(8)" alt="">
          <img class="channel" :src="pic[9]" @click="changeFrame(9)" alt="">
          <img class="channel" :src="pic[10]" @click="changeFrame(10)" alt="">
          <img class="channel" :src="pic[11]" @click="changeFrame(11)" alt="">
          <img class="channel" :src="pic[12]" @click="changeFrame(12)" alt="">
          <img class="channel" :src="pic[13]" @click="changeFrame(13)" alt="">
          <img class="channel" :src="pic[14]" @click="changeFrame(14)" alt="">
          <img class="channel" :src="pic[15]" @click="changeFrame(15)" alt="">
          <img class="channel" :src="pic[16]" @click="changeFrame(16)" alt="">
    </div>
      <div class="panels-foot"></div>
    </div>


  </div>
</template>

<script>
import {state} from "@/store/state";

export default {
name: "Panel",
  components: {},
  data(){
    return{pic:{
      1:state.unsignalImg,
      2:state.unsignalImg,
      3:state.unsignalImg,
      4:state.unsignalImg,
      5:state.unsignalImg,
      6:state.unsignalImg,
      7:state.unsignalImg,
      8:state.unsignalImg,
      9:state.unsignalImg,
      10:state.unsignalImg,
      11:state.unsignalImg,
      12:state.unsignalImg,
      13:state.unsignalImg,
      14:state.unsignalImg,
      15:state.unsignalImg,
      16:state.unsignalImg,},
      unsignalImg:state.unsignalImg,
      signImg: state.signalImg
    }
  },
  methods:{
    changeFrame(data){
      if(state.antselect[data-1]){
        state.antselect[data-1]=false
        this.pic[data] = this.unsignalImg
      }else {
        state.antselect[data-1]=true
        this.pic[data] = this.signImg
      }
    },
    refreshCharts(){
      for(let i=0;i<16;i++){
        state.antselect[i] = false
        this.pic[i] = require('../assets/unsign.png')
      }
    }
  }
}
</script>

<style scoped>
.channel{
  width: 25%;
  height: auto;
  aspect-ratio:1/1;
  border: 2px solid #04254E;
}
.panels{
  position: relative;
  min-height: 250px;
  height: auto !important;
  width: 100%;
  border: 1px solid #999999;
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
