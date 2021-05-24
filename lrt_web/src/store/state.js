import { reactive } from "vue";
// const trainImg = "image://"+require('@/assets/train.png')
const computerImg = "image://"+require('@/assets/gui.png')
const serverImg = 'image://'+require('@/assets/server.png')
const gatewayImg = 'image://'+require('@/assets/gateway.png')
const dataImg = 'image://'+require('@/assets/database.png')
export const state = reactive({
    antselect:[false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,],
    connected:false,
    localOpition:{
        animation:false,
        title: {text: 'Localization', textStyle: {color: "#fff"}, left: "center"},
        tooltip: {
            formatter:'{a}<br/>{c}',
            axisPointer: {
                type: 'none',
                label: {
                    backgroundColor: 'white'
                }
            }
        },
        legend: {
            type: 'scroll',
            data: [],
            orient: 'vertical',
            y: '10%',
            x: 'right',
            selectedMode: false,
            // textStyle:{color:"#fff"},
        },
        xAxis: {
            scale: true,
        },
        yAxis: {
            scale: true,
        },
        series: []},
    phaseOpition:{
        // aanimation:false,
        title: {
            text: 'Phase',
            textStyle:{color:"#fff"},
            left: "center"
        },
        tooltip: {
            trigger: 'axis',
        },
        legend: {
            type: 'scroll',
            data: ['ANT1', 'ANT2', 'ANT3', 'ANT4', 'ANT5','ANT6', 'ANT7', 'ANT8', 'ANT9', 'ANT10','ANT11', 'ANT12', 'ANT13'
                , 'ANT14', 'ANT15','ANT16'],
            orient: 'vertical',
            y: 'center',
            x: 'right',
            selectedMode: false,
            // textStyle:{color:"#fff"},
        },
        grid: {
            left: '3%',
            right: '15%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            // feature: {
            //     saveAsImage: {}
            // }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: [],
            show:false
        },
        yAxis: {
            type: 'value',
            show:true
        },
        series: [
            {
                name: 'ANT1',
                smooth:true,
                symbol: 'none',
                type: 'line',
                stack: 'phase',
                data: []
            },
            {
                name: 'ANT2',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT3',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT4',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT5',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT6',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT7',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT8',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT9',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT10',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT11',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT12',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT13',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT14',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT15',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT16',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'phase',
                data: []
            }
        ]
    },
    rssOpition:{
        series: [{
            min:-90,
            max:-50,
            type: 'gauge',
            radius: '20%',
            center: ['10%', '15%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                },
            },
            splitLine: {
                show:false
            },
            axisLabel: {
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['10%', '40%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['10%', '65%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['10%', '90%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['38%', '15%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle:{
                    color:'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['38%', '40%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['38%', '65%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['38%', '90%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['64%', '15%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['64%', '40%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['64%', '65%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['64%', '90%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['90%', '15%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['90%', '40%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['90%', '65%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },{
            min:-90,
            max:-50,
            name:'rss1',
            type: 'gauge',
            radius: '20%',
            center: ['90%', '90%'],
            axisTick:{
                show:false
            },
            axisLine: {
                lineStyle: {
                    width: 5,
                    color: [
                        [0.25, '#fd666d'],
                        [0.5, '#D7B599'],
                        [0.75, '#67e0e3'],
                        [1, '#17C37B']
                    ]
                }
            },
            pointer: {
                itemStyle: {
                    color: 'inherit'
                }

            },
            splitLine: {
                distance: -30,
                length: 30,
                lineStyle: {
                    color: '#fff',
                    width: 4
                },
                show:false
            },
            axisLabel: {
                color: 'auto',
                distance: 40,
                fontSize: 20,
                show:false
            },
            detail:{
                show:false
            },
            data: [-70]
        },]
    },
    spectrumOpition:{
        title: {text: 'Spectrum', textStyle: {color: "#fff"}, left: "center"},
        tooltip: {},
        grid: {
            height: '80%',
            width: '50%',
            top: '10%',
            left:"center",
        },
        xAxis: {
            type: 'category',
            min:0,
            max:100
        },
        yAxis: {
            type: 'category',
            min:0,
            max:100
        },
        visualMap: {
            y: 'center',
            x: 'right',
            min: 0,
            max: 255,
            calculable: true,
            realtime: false,
            inRange: {
                // color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
                color:['#04254E','#25255F','#5954A4','#DFA0C8','#33C7F7','#8AD5EB','#C2E3F4']
            }
        },
        series: [{
            progressiveThreshold: 20000,
            name: 'Gaussian',
            type: 'heatmap',
            data: [],
            emphasis: {
                itemStyle: {
                    borderColor: '#333',
                    borderWidth: 1
                }
            },
            progressive:2000,
            animation: false
        }]
    },
    rsslineOpition:{
        title: {
            text: 'RSS',
            textStyle:{color:"#fff"},
            left: "center"
        },
        tooltip: {
            trigger: 'axis',
        },
        legend: {
            type: 'scroll',
            data: ['RSS1', 'RSS2', 'RSS3', 'RSS4', 'RSS5','RSS6', 'RSS7', 'RSS8', 'RSS9', 'RSS10','RSS11', 'RSS12', 'RSS13'
                , 'RSS14', 'RSS15','RSS16'],
            orient: 'vertical',
            y: 'center',
            x: 'right',
            selectedMode: false,
            // textStyle:{color:"#fff"},
        },
        grid: {
            left: '3%',
            right: '15%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            // feature: {
            //     saveAsImage: {}
            // }
        },
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: [],
            show:false
        },
        yAxis: {
            type: 'value',
            show: true,
            min:-90,
            max:-50
        },
        series: [
            {
                name: 'RSS1',
                smooth:true,
                symbol: 'none',
                type: 'line',
                stack: 'rss',
                data: []
            },
            {
                name: 'RSS2',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS3',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS4',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS5',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS6',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS7',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS8',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS9',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS10',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS11',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS12',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS13',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS14',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS15',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS16',
                type: 'line',
                smooth:true,
                symbol: 'none',
                stack: 'rss',
                data: []
            }
        ]
    },
    radarOpition: {
        animation:false,
        backgroundColor: 'rgba(0,0,0,0)',
        polar: {},
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross'
            }
        },
        angleAxis: {
            type: 'value',
            startAngle: 0,
            min:0,
            max:360,
            axisLine:{
                lineStyle:{
                    color:'rgba(3, 177, 0, 0.4)',
                    width:3
                }
            },
            splitLine:{
                lineStyle:{
                    color:'rgba(3, 177, 0, 0.4)',
                    width:3
                }
            }


        },
        radiusAxis: {
            min:0,
            max:1,
            show:true,
            axisLine:{
                lineStyle:{
                    color:'rgba(3, 177, 0, 0.4)',
                    width:3
                }
            },
            splitLine:{
                lineStyle:{
                    color:'rgba(3, 177, 0, 0.4)',
                    width:3
                }
            }


        },
        series: [{
            coordinateSystem: 'polar',
            name: 'gateway1',
            data: [],
            type:'effectScatter',
            // symbol: trainImg,
            // symbolSize:[20,20],
            // showAllSymbol:true,
            color:'red'

        },
            {
                coordinateSystem: 'polar',
                name: 'gateway2',
                data: [],
                type:'effectScatter',
                // symbol: trainImg,
                // symbolSize:[20,20],
                // showAllSymbol:true,
                color:'#fc5404'

            }]
    },
    topologyOpition:{
        title: {
            text: '{aaa|    Chrysanth LRT Net}',
            left:'5%',
            top:'center',
            textStyle:{

                rich:{
                    aaa:{
                        fontSize:50,
                        backgroundColor:{image:require('@/assets/flower.png')},
                        height:200,
                        width:200,
                    }
                }
            }
        },
        grid: {
            height: '80%',
            width: '50%',
            top: '0',
            left:"center",
        },
        tooltip: {},
        animationDurationUpdate: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [
            {
                type: 'graph',
                layout: 'none',
                symbolSize: 50,
                roam: false,
                label: {
                    show: true,
                },
                edgeSymbol: 'circle',
                edgeSymbolSize: [10, 10],
                edgeLabel: {
                    fontSize: 10,
                },
                data: [{
                    name: 'Database',
                    x: 50,
                    y: 30,
                    symbol: dataImg,
                    symbolSize:[100,100],
                    showAllSymbol:true,

                },{
                    name: 'GUI Server',
                    x: 200,
                    y: 30,
                    symbol: serverImg,
                    symbolSize:[100,100],
                    showAllSymbol:true,

                },{
                    name: 'GUI',
                    x: 400,
                    y: 30,
                    symbol: computerImg,
                    symbolSize:[100,100],
                    showAllSymbol:true,

                }, {
                    name: 'X Server',
                    x: 300,
                    y: 200,
                    symbol: serverImg,
                    symbolSize:[100,100],
                    showAllSymbol:true,
                }, {
                    name: 'Gateway1',
                    x: 200,
                    y: 500,
                    symbol: gatewayImg,
                    symbolSize:[100,100],
                    showAllSymbol:true,
                }, {
                    name: 'Gateway2',
                    x: 400,
                    y: 500,
                    symbol: gatewayImg,
                    symbolSize:[100,100],
                    showAllSymbol:true,
                }],
                // links: [],
                links: [{
                    source: 'GUI',
                    target: 'X Server',
                    lineStyle: {
                        opacity: 1,
                        width: 5,
                        curveness: 0.5,
                        color:'#007580',
                    }
                }, {
                    source: 'X Server',
                    target: 'Gateway1',
                    lineStyle: {
                        opacity: 1,
                        width: 5,
                        curveness: -0.5,
                        color:'#007580',
                    }
                }, {
                    source: 'X Server',
                    target: 'Gateway2',
                    lineStyle: {
                        opacity: 1,
                        width: 5,
                        curveness: -0.5,
                        color:'#007580',
                    }
                },{
                    source: 'X Server',
                    target: 'GUI Server',
                    lineStyle: {
                        opacity: 1,
                        width: 5,
                        curveness: -0.5,
                        color:'#007580',
                    }
                },{
                    source: 'Database',
                    target: 'GUI Server',
                    lineStyle: {
                        opacity: 1,
                        width: 5,
                        curveness: 0,
                        color:'#007580',
                    }
                },{
                    source: 'GUI',
                    target: 'GUI Server',
                    lineStyle: {
                        opacity: 1,
                        width: 5,
                        curveness: 0,
                        color:'#007580',
                    }
                }],

            }
        ]
    },
    rss:{},
    phase:{},
    rssLine:{},
    aoa:{},
    gatewayChoose:'gateway1',
    // tagList: [],
})
