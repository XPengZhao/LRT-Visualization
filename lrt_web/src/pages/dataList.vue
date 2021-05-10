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
      <tbody style="color: black">
      <tr>
        <th scope="row">1</th>
        <td>
          <img :src='connectimg' style="max-height: 100px">
        </td>
        <td style="max-height:100px;vertical-align: middle;">
          <a type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample" >
          test1
          </a>
          <div class="collapse" id="collapseExample" style="position: relative">
            <div class="card card-body row" style="max-width: 200px;max-height: 50px; left: 20px">
              <img :src='updateimg' style="height: auto;width: 20px;aspect-ratio:1/1;">
              <img :src='deleteimg' style="height: auto;width: 20px;aspect-ratio:1/1;">
            </div>
          </div>
        </td>

        <td>@mdo</td>

      </tr>

      <tr>
        <th scope="row">2</th>
        <td>Jacob</td>
        <td>Thornton</td>
        <td>@fat</td>
      </tr>
      <tr>
        <th scope="row">3</th>
        <td>Larry</td>
        <td>the Bird</td>
        <td>@twitter</td>
      </tr>
      </tbody>
    </table>
  </div>



</template>

<script>
import {useRouter} from "vue-router";

export default {
  name: "dataList",
  data(){
    return{
      updateimg:require('@/assets/update.png'),
      deleteimg:require('@/assets/delete.png'),
      connectimg:require('@/assets/connect.png'),
      flowerimg:require('@/assets/flower.png'),
    }
  },
  setup(){
    const router = useRouter()
    const toHome=(()=>{
      router.push({
        name: 'home'
      })
    })
    return{
      toHome
    }
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
}
</style>
