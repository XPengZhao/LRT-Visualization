<template>
  <div ref="main" style="min-height: 800px;min-width: 800px"></div>
</template>

<script>
import axios from "axios";
let echarts = require("echarts/lib/echarts");
import 'zrender/lib/svg/svg';
import { TooltipComponent } from 'echarts/components';
echarts.use([TooltipComponent]);
import { TitleComponent } from 'echarts/components';
echarts.use([TitleComponent]);
import { VisualMapComponent } from 'echarts/components';
echarts.use([VisualMapComponent]);
import { ParallelComponent } from 'echarts/components';
echarts.use([ParallelComponent]);
import { ToolboxComponent } from 'echarts/components';
echarts.use([ToolboxComponent]);
export default {
  name: 'HelloWorld',
  data(){
    return{
      ROOT_PATH:'https://cdn.jsdelivr.net/gh/apache/echarts-website@asf-site/examples',
      option:{},
      indices : {
        name: 0,
        group: 1,
        id: 16
      },
      schema : [
        {name: 'name', index: 0},
        {name: 'group', index: 1},
        {name: 'protein', index: 2},
        {name: 'calcium', index: 3},
        {name: 'sodium', index: 4},
        {name: 'fiber', index: 5},
        {name: 'vitaminc', index: 6},
        {name: 'potassium', index: 7},
        {name: 'carbohydrate', index: 8},
        {name: 'sugars', index: 9},
        {name: 'fat', index: 10},
        {name: 'water', index: 11},
        {name: 'calories', index: 12},
        {name: 'saturated', index: 13},
        {name: 'monounsat', index: 14},
        {name: 'polyunsat', index: 15},
        {name: 'id', index: 16}
      ],
      groupCategories : [],
      groupColors : [],
      resData : []
    }
  },
  mounted() {
      this.init()
    },
  methods:{
      normalizeData(originData) {
        const that = this
        var groupMap = {};
        originData.forEach(function (row) {
          var groupName = row[that.indices.group];
          if(groupMap){
            if (!(groupName in groupMap)) {
              groupMap[groupName] = 1;
            }
          }
        });

        originData.forEach(function (row) {
          row.forEach(function (item, index) {
            if (index !== that.indices.name
                && index !== that.indices.group
                && index !== that.indices.id
            ) {
              // Convert null to zero, as all of them under unit "g".
              row[index] = parseFloat(item) || 0;
            }
          });
        });

        for (var groupName in groupMap) {
          if (groupName in groupMap) {
            this.groupCategories.push(groupName);
          }
        }
        var hStep = Math.round(300 / (this.groupCategories.length - 1));
        for (var i = 0; i < this.groupCategories.length; i++) {
          this.groupColors.push(echarts.color.modifyHSL('#5A94DF', hStep * i));
        }

      },
      init(){
        var lineStyle = {
            width: 0.5,
            opacity: 0.05

        };
        var chartDom = this.$refs.main;
        this.myChart = echarts.init(chartDom, null, {renderer: 'svg'});
        const that = this
        axios.get('/data/nutrients-sample.json').then(function (res) {
          console.log(res.data)
          that.normalizeData(res.data);
          that.myChart.setOption({
            backgroundColor: '#333',
            tooltip: {
              padding: 10,
              backgroundColor: '#222',
              borderColor: '#777',
              borderWidth: 1
            },
            title: [
              {
                text: 'Groups',
                top: 0,
                left: 0,
                textStyle: {
                  color: '#fff'
                }
              }
            ],
            toolbox:{
              feature:{
                saveAsImage:{
                  show:true,
                  type:'svg'
                }
              },
              iconStyle:{
                color:'white',
                borderColor: 'white',

              }
            },
            visualMap: {
              show: true,
              type: 'piecewise',
              categories: that.groupCategories,
              dimension: that.indices.group,
              inRange: {
                color: that.groupColors //['#d94e5d','#eac736','#50a3ba']
              },
              outOfRange: {
                color: ['#ccc'] //['#d94e5d','#eac736','#50a3ba']
              },
              top: 20,
              textStyle: {
                color: '#fff'
              },
              realtime: false
            },
            parallelAxis: [
              {dim: 16, name: that.schema[16].name, scale: true, nameLocation: 'end'},
              {dim: 2, name: that.schema[2].name, nameLocation: 'end'},
              {dim: 4, name: that.schema[4].name, nameLocation: 'end'},
              {dim: 3, name: that.schema[3].name, nameLocation: 'end'},
              {dim: 5, name: that.schema[5].name, nameLocation: 'end'},
              {dim: 6, name: that.schema[6].name, nameLocation: 'end'},
              {dim: 7, name: that.schema[7].name, nameLocation: 'end'},
              {dim: 8, name: that.schema[8].name, nameLocation: 'end'},
              {dim: 9, name: that.schema[9].name, nameLocation: 'end'},
              {dim: 10, name: that.schema[10].name, nameLocation: 'end'},
              {dim: 11, name: that.schema[11].name, nameLocation: 'end'},
              {dim: 12, name: that.schema[12].name, nameLocation: 'end'},
              {dim: 13, name: that.schema[13].name, nameLocation: 'end'},
              {dim: 14, name: that.schema[14].name, nameLocation: 'end'},
              {dim: 15, name: that.schema[15].name, nameLocation: 'end'}
            ],
            parallel: {
              left: 280,
              top: 20,
              // top: 150,
              // height: 300,
              width: 400,
              layout: 'vertical',
              parallelAxisDefault: {
                type: 'value',
                name: 'nutrients',
                nameLocation: 'end',
                nameGap: 20,
                nameTextStyle: {
                  color: '#fff',
                  fontSize: 14
                },
                axisLine: {
                  lineStyle: {
                    color: '#aaa'
                  }
                },
                axisTick: {
                  lineStyle: {
                    color: '#777'
                  }
                },
                splitLine: {
                  show: false
                },
                axisLabel: {
                  color: '#fff'
                },
                realtime: false
              }
            },
            animation: false,
            series: [
              {
                name: 'nutrients',
                type: 'parallel',
                lineStyle: lineStyle,
                inactiveOpacity: 0,
                activeOpacity: 0.01,
                progressive: 200,
                smooth: true,
                data: res.data
              }
            ]
          })
        });

      },

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
