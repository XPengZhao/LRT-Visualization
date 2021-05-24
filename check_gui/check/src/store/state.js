import { reactive } from "vue";

export const state = reactive({
    checkOpition:{
        title: {
            left:'center',
            text: 'EPC space',
            textStyle:{
                color:'white',
                fontSize:30
            },
        },
        visualMap: {
            top:'center',
            left:'5%',
            show: true,
            min: 1,
            max: 10,
            text: ['10', '1'],
            inRange: {
                symbolSize: [25, 1],
                color: ['#a50026','#d73027','#f46d43','#fdae61','#fee090','#ffffbf','#e0f3f8','#abd9e9','#74add1','#4575b4','#313695'],
            }
        },
        xAxis3D: {
            type: 'value'
        },
        yAxis3D: {
            type: 'value'
        },
        zAxis3D: {
            type: 'value'
        },
        grid3D: {
            top:-50,
            width:'100%',
            axisLine: {
                lineStyle: { color: '#fff' }
            },
            axisPointer: {
                lineStyle: { color: '#fff' }
            },
            viewControl: {
                // autoRotate: true
            }
        },
        series: [{
            type: 'scatter3D',
            data:[],
        },
            {
                type: 'scatter3D',
                data:[],
                itemStyle: {
                    color:'white',		   		//点颜色
                    borderColor: 'white',  		//点边框颜色
                    opacity: 0,            		//点的透明度 1不透明
                    borderWidth: 30     		//图形描边宽度
                },
            }]
    },
    spectrumOpition:{
        title: {text: 'Spectrum', textStyle: {color: "#fff"}, left: "center"},
        tooltip: {},
        grid: {
            height: '80%',
            width: '90%',
            top: '10%',
            left:"center",
        },
        xAxis: {
            type: 'category',
            min:0,
            max:360
        },
        yAxis: {
            type: 'category',
            min:0,
            max:90
        },
        visualMap: {
            y: 'center',
            x: 'right',
            min: 0,
            max: 1,
            calculable: true,
            realtime: false,
            inRange: {
                // color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
                color:['#04254E','#25255F','#5954A4','#DFA0C8','#33C7F7','#8AD5EB','#C2E3F4']
            }
        },
        series: [{
            progressiveThreshold: 10000,
            name: 'Gaussian',
            type: 'heatmap',
            data: [],
            emphasis: {
                itemStyle: {
                    borderColor: '#333',
                    borderWidth: 1
                }
            },
            progressive:10000,
            animation: false
        }]
    },
    antPos:[[-0.6,0.8],[-0.6,0],[-0.6,-0.8],[0,0.4],[0.6,0.8],[0.6,0],[0.6,-0.8],[-0.4,0]]
})
