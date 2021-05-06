<template>
  <div class=" mt-2">
    <div class="card panels" style="background-color: #100C2A" >
      <div class="card-body">
          <img class="channel" :src="pic[1]" @click="changeFrame(1)">
          <img class="channel" :src="pic[2]" @click="changeFrame(2)">
          <img class="channel" :src="pic[3]" @click="changeFrame(3)">
          <img class="channel" :src="pic[4]" @click="changeFrame(4)">
          <img class="channel" :src="pic[5]" @click="changeFrame(5)">
          <img class="channel" :src="pic[6]" @click="changeFrame(6)">
          <img class="channel" :src="pic[7]" @click="changeFrame(7)">
          <img class="channel" :src="pic[8]" @click="changeFrame(8)">
          <img class="channel" :src="pic[9]" @click="changeFrame(9)">
          <img class="channel" :src="pic[10]" @click="changeFrame(10)">
          <img class="channel" :src="pic[11]" @click="changeFrame(11)">
          <img class="channel" :src="pic[12]" @click="changeFrame(12)">
          <img class="channel" :src="pic[13]" @click="changeFrame(13)">
          <img class="channel" :src="pic[14]" @click="changeFrame(14)">
          <img class="channel" :src="pic[15]" @click="changeFrame(15)">
          <img class="channel" :src="pic[16]" @click="changeFrame(16)">
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
      1:require('../assets/unsign.png'),
      2:require('../assets/unsign.png'),
      3:require('../assets/unsign.png'),
      4:require('../assets/unsign.png'),
      5:require('../assets/unsign.png'),
      6:require('../assets/unsign.png'),
      7:require('../assets/unsign.png'),
      8:require('../assets/unsign.png'),
      9:require('../assets/unsign.png'),
      10:require('../assets/unsign.png'),
      11:require('../assets/unsign.png'),
      12:require('../assets/unsign.png'),
      13:require('../assets/unsign.png'),
      14:require('../assets/unsign.png'),
      15:require('../assets/unsign.png'),
      16:require('../assets/unsign.png'),}
    }
  },
  methods:{
    changeFrame(data){
      if(state.antselect[data-1]){
        state.antselect[data-1]=false
        this.pic[data] = require('../assets/unsign.png')
      }else {
        state.antselect[data-1]=true
        this.pic[data] = require('../assets/sign.png')
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
  min-height: 410px;
  width: 100%;
  border: 1px solid #999999;
}
.panels::before{
  position: absolute;
  top: 0;
  left: 0;
  width: 20px;
  height: 20px;
  border-left: 3px solid #999999;
  border-top: 3px solid #999999;
  content: "";
}
.panels::after{
  position: absolute;
  top: 0;
  right: 0;
  width: 20px;
  height: 20px;
  border-right: 3px solid #999999;
  border-top: 3px solid #999999;
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
  border-left: 3px solid #999999;
  border-bottom: 3px solid #999999;
  content: "";
}
.panels-foot::after{
  position: absolute;
  bottom: 0;
  right: 0;
  width: 20px;
  height: 20px;
  border-right: 3px solid #999999;
  border-bottom: 3px solid #999999;
  content: "";
}
</style>
