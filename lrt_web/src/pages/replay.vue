<template>
  <nav class="navbar navbar-expand-lg" style="background-color: #04254E;">
    <a class="navbar-brand" href="#"  style=" color: white;" @click="toHome()">
      <img :src="flowerimg" style="height: 30px">
      Chrysanth LRT
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <vue-slider v-model="indexValue"
                    :width="1000"
                    :lazy="true"
                    @change="replayUpdate"
                    :min-range="10"
                    :max-range="replayDataLength"
                    :max = "replayDataLength"
                    :tooltip = "'always'"
                    :tooltip-placement="'bottom'"
                    ref="timeSlider"
                    id = "timeSlider"
        />
      </div>
    </div>
    <button type="button" id="fullButton" class="btn" style="background-color: #04254E;color: white;min-width: 20px;position: relative;right: 0"  data-toggle="button" aria-pressed="false" @click="changeScreen()">
      <img :src="windowSizeImg" style="height: 20px">
    </button>
  </nav>
  <div class="mainBox row mt-3">
    <span class="col-2"></span>
    <div class="col-6 mt-2">
      <Localization ref="local"></Localization>
    </div>
  </div>
</template>

<script>

import {state} from "../store/state";
import Localization from "../components/Localization";
import screenfull from "screenfull";

export default {
  name: "replay",
  components:{Localization, VueSlider: window['vue-slider-component']},
  data(){
    return{
      flowerimg:require('@/assets/flower.png'),
      indexValue:[0,200],
      replayDataLength:1000,
      isFullscreen: false,
    }
  },
  computed:{
    windowSizeImg(){
      return this.isFullscreen?require('@/assets/window.png'):require('@/assets/fullScreen.png')
    },
  },
  created() {
    this.replayDataLength=state.replayLength
  },
  mounted() {
    this.$refs.local.initLocalizationCharts()
    this.replayUpdate()
  },
  methods:{
    changeScreen(){
      if (!screenfull.isEnabled) return alert(`Error`);
      this.isFullscreen = !this.isFullscreen
      screenfull.toggle();
    },
    replayUpdate(){
        this.$refs.local.replayChart(this.indexValue)
    }
  }

}
</script>

<style scoped>

</style>