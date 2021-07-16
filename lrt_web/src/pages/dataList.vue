<template>
  <nav class="navbar navbar-expand-lg" style="background-color: #04254E;">
    <a class="navbar-brand" href="#"  style=" color: white;" @click="toHome()">
      <img :src="flowerimg" style="height: 30px">
      Chrysanth LRT
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
  </nav>
  <div class="mainBox" style="background-color: #fcecdd">
    <table class="table">
      <thead class="thead" style="background-color: #fea82f">
      <tr>
        <th scope="col">#</th>
        <th scope="col">Image</th>
        <th scope="col">Time</th>
        <th scope="col">Describe</th>
      </tr>
      </thead>
      <tbody style="color: black" id='table'>
      </tbody>

    </table>
  </div>
  <div id="updateTable" class="updateTable">
    <div class="tableCard  animate__animated animate__backInLeft" id = 'tableCard'>
      <div class="card" style="border: 2px solid #151515">
        <div class="card-header row" id="experimentID" style="background-color: #3c415c;color: white">
          <h5 class="col-11" id="etim">Experiment Time:</h5>
          <img :src="closeImg" class="col-1" style="border:2px solid white;border-radius:50px;height: 20px;width: 20px" @click="closeDiv()">
        </div>
        <div class="card-body" style="background-color: #b4a5a5;color: #3c415c">
          <div class="row" id="chooseImg">
            <input type="file" accept="image/*" v-on:change="uploadImg($event)" v-show="false" id="describeImgArea"/>
            <div class="ml-3 uploadLabel">Upload</div>
            <label id="describeImgPath" class="col-8 uploadPath" style="color: #3c415c"></label>
            <button class="btn uploadButton" v-on:click="callUpImg()">Choose</button>
          </div>
          <div>
            <img alt="" id="imgShow" style="height: 200px">
          </div>
          <hr>
          <div style="width: 100%">
            <h5 class="card-title">Describe</h5>
            <textarea id="describeWord" style="width: 80%;color: black;background-color: rgba(255,255,255,0.17)" rows="5" cols="33" ></textarea>
          </div>
          <hr>
          <button class="btn sendButton" v-on:click="sendTable()">Send</button>
        </div>
      </div>
    </div>
  </div>




</template>

<script>
import {useRouter} from "vue-router";
import axios from "axios";
import {state} from "@/store/state";
/* eslint-disable */
export default {
  name: "dataList",
  data() {
    return {
      connectimg: require('@/assets/connect.png'),
      flowerimg: require('@/assets/flower.png'),

    }
  },
  mounted() {
    this.create()
    this.getTable()
    $('#updateTable').hide()
    sessionStorage.setItem('valueURL','null')
  },
  setup(){
    const closeImg = require('@/assets/close.png')
    const router = useRouter()
    const BackendUrl=localStorage.getItem("BackendUrl")
    const updateimg=require('@/assets/update.png'),
        deleteimg=require('@/assets/delete.png'),
        playimg = require('@/assets/play.png'),
        analysisimg = require("@/assets/analysis.png")
    var dataListRes = []
    const toHome=(()=>{
      router.push({
        name: 'home'
      })
    })
    const updateTable=((e)=>{
      $('#tableCard').removeClass('animate__backOutDown')
      let arr = e.split('0128')
      $('#etim').html('Experiment Time:'+arr[0])
      $('#describeWord').val(arr[1])
      if (arr[2]=='null'){
        $('#chooseImg').show()
        $('#imgShow').hide()
      }else {
        $('#chooseImg').hide()
        $('#imgShow').attr('src',arr[2])
        $('#imgShow').show()
      }
      $('#updateTable').show()
    })
    const deleteTable=((e)=>{
      axios.post(BackendUrl+'/deleteTable',{
        tableName:e
      }).then(function (){
        $('#table').empty()
        getTable()
      }).catch(function (err) {
        console.log(err)
      });
    })
    const getTable=(()=>{
      axios.post(BackendUrl+'/searchData', {
        mes: 0
      }).then(function (res) {
        for (let i = 0; i < res.data.length; i++) {
          $('#table').append('<tr>' +
              '<th scope="row">' + (i + 1) + '</th>' +
              '        <td>' +
              '          <img src="' + res.data[i].img + '" alt="" style="height: 300px">' +
              '        </td>' +
              '        <td style="max-height:100px;vertical-align: middle;">' +
              '          <a type="button" data-toggle="collapse" data-target="#collapseExample' + i + '" aria-expanded="false" aria-controls="collapseExample" >\n' +
              '            ' + res.data[i].tableName + '' +
              '          </a>' +
              '          <div class="collapse" id="collapseExample' + i + '" style="position: relative">\n' +
              '            <div class="card card-body row" style="max-width: 200px;max-height: 50px; left: 20px">' +
              "              <a class='updatelink' onclick='updateTable(\"" + res.data[i].tableName+"0128"+res.data[i].Describe+"0128"+res.data[i].img+ "\")'>" +
              '               <img src="' + updateimg + '" alt="" style="border:1px solid black;border-radius: 5px;height:20px;width:20px;"></a>' +
              // "              <a class='deletelink' onclick='deleteTable(\""+res.data[i].tableName+"\")'>" +
              // '              <img src="' + deleteimg + '" alt="" style="border:1px solid black;border-radius: 5px;height:20px;width:20px;"></a>' +
              "              <a class='replay' onclick='replay(\""+res.data[i].tableName+"\")'>" +
              '              <img src="' + playimg + '" alt="" style="border:1px solid black;border-radius: 5px;height:20px;width:20px;"></a>' +
              "              <a class='analysis' onclick='analysis(\""+res.data[i].tableName+"\")'>" +
              '              <img src="' + analysisimg + '" alt="" style="border:1px solid black;border-radius: 5px;height:20px;width:20px;"></a>' +
              '            </div>' +
              '          </div>' +
              '        </td>' +
              '        <td style="max-height:100px;vertical-align: middle;">' + res.data[i].Describe + '</td>' +
              '      </tr>')
        }
      }).catch(function (err) {
        console.log(err)
      });
    })
    const create=(()=>{
      window.updateTable = updateTable
      window.deleteTable = deleteTable
      window.replay = replay
      window.analysis= analysis
    })
    const replay=((e)=>{
      axios.post(BackendUrl+'/replay',{
        table:e
      }).then(function (res) {
        state.replayLength = Number(res.data.len)
        state.replay = res.data.message
        setTimeout(goReplay,100)
      })

    })
    const analysis=(async (e)=>{
     sessionStorage.setItem('tableName',e)
      goAnalysis()
    })

    const callUpImg=(()=>{
      $('#describeImgArea').click()
    })
    const uploadImg=((e)=>{
      let file = e.target.files[0]
      var reader = new FileReader()
      reader.readAsDataURL(file)
      reader.onload = function (){
        sessionStorage.valueURL=this.result
      }
      $('#describeImgPath').html(file.name)

    })
    const sendTable=(()=>{
      console.log(sessionStorage.getItem('valueURL'))
    })
    const closeDiv=(()=>{
      $('#etim').html('')
      $('#describeWord').val('')
      $('#imgShow').attr('src','')
      sessionStorage.setItem('valueURL','')
      $('#tableCard').addClass('animate__backOutDown')
      setTimeout(function (){
        $('#updateTable').hide()
      },1000)
    })
    const goDraw=(()=>{
      router.push({
        name: 'Show'
      })
    })
    const goAnalysis=(()=>{
      router.push({
        name: 'Analysis'
      })
    })
    const goReplay=(()=>{
      router.push({
        name: 'Replay'
      })
    })
    return{
      create,getTable,deleteTable,updateTable,toHome,callUpImg,uploadImg,sendTable,closeImg,closeDiv,replay,goDraw,BackendUrl,goAnalysis,analysis,goReplay,updateimg,analysisimg,playimg,dataListRes
    }
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
}
.updateTable{
  overflow: hidden;
  font-family: 'Ubuntu', sans-serif;
  width: 600px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
  z-index: 999;

}
.tableCard{
  font-weight: 700;
  text-align: center;
}
.uploadLabel{
  height:40px;
  width:80px;
  text-align: center;
  line-height:40px;
  background-color: #3c415c;
  border-radius: 5px;
  color: white
}
.uploadButton{
  background-color: #3c415c;
  border-radius: 5px;
  color: white;
  height:40px;
}
.uploadPath{
  color: #3c415c;
  height:40px;
  text-align: center;
  line-height:40px;
  border-bottom: 1px solid #151515;
}
.sendButton{
  width: 100px;
  color: white;
  background-color: #3c415c;
  border-radius: 5px;
}
.updatelink{}
.deletelink{}
</style>
