import { reactive } from "vue";
// const trainImg = "image://"+require('@/assets/train.png')
const atnPic="path://M482.1,293.3h60.8V677h-60.8z M512.5,617.1l-30.4-23.8v83.8h60.8v-83.8z M482.1,293.3v110.5c9.8,2,20,3,30.4,3,10.4,0,20.6-1,30.4-3V293.3h-60.8z "+
    "M421.57,567.208L703.51,788.18l-37.508,47.856-281.94-220.974z "+
"M504,631.7l-49.3,38.7L504,709l49.3-38.6z "+
"M392.1,604.9l-3.8,13.4 51.7,40.5,17.9-63.2-36.2-28.4z "+
"M526.3,649.2L477,687.8l49.3,38.7,49.3-38.7z "+
"M603.408,567.172l37.508,47.856L358.976,836l-37.507-47.855z "+
"M335.3,805.6l23.8,30.4,39.5-31,28.2-99.4-81.3,63.7z M603.4,567.2l-36.3,28.4,17.9,63.2,51.8-40.5-3.8-13.4z M679.5,769.3l-81.2-63.7,28.1,99.4,39.6,31 23.8-30.4z "+
"M687.2,932.3L512.5,315.6,337.9,932.3l-58.5-16.6,203.9-720c3.7-13.1,15.7-22.1,29.3-22.1,13.6,0,25.5,9,29.3,22.1l203.9,720-58.6,16.6z"+
"M541.8,195.7c-3.7-13.1-15.7-22.1-29.3-22.1-13.6,0-25.5,9-29.3,22.1l-55.9,197.4c17.2,10.5,36.5,17.9,57.1,21.5l28-99,28,99c20.6-3.6,39.9-11,57.1-21.5l-55.7-197.4z "+
"M512.5,253.5m-109.6,0a109.6,109.6,0,1,0,219.2,0,109.6,109.6,0,1,0-219.2,0Z,"+
"M369,384.1c-4.1,0-8.3-1.8-11.1-5.3-28.6-35.3-44.4-79.8-44.4-125.3s15.8-90,44.4-125.2c5-6.1,13.9-7.1,20.1-2.1,6.1,5,7,13.9,2.1,20-24.5,30.2-38,68.3-38,107.3s13.5,77.1,38,107.3c5,6.1,4,15.1-2.1,20.1-2.6,2.1-5.8,3.2-9,3.2z "+
"M299,440.8c-4.1 0-8.3-1.8-11.1-5.3-41.6-51.3-64.5-115.9-64.5-182s22.9-130.7,64.5-182c5-6.1,13.9-7.1,20-2.1s7,13.9,2.1,20c-37.5,46.2-58.1,104.5-58.1,164s20.6,117.8,58.1,164c5,6.1,4,15.1-2.1,20-2.6,2.3-5.7,3.4-8.9,3.4z M656,384.1c-3.2,0-6.3-1-9-3.2-6.1-5-7-13.9-2.1-20.1,24.5-30.2,38-68.3,38-107.3s-13.5-77.1-38-107.3c-5-6.1-4-15.1,2.1-20,6.1-5,15.1-4,20.1,2.1,28.6,35.3,44.4,79.8,44.4,125.2,0,45.5-15.8,90-44.4,125.3-2.8,3.5-6.9,5.3-11.1,5.3z "+
"M726.1,440.8c-3.2,0-6.3-1-9-3.2-6.1-5-7-13.9-2.1-20,37.5-46.2,58.1-104.5,58.1-164,0-59.6-20.6-117.8-58.1-164-5-6.1-4-15.1 2.1-20,6.1-5,15.1-4,20,2.1,41.6,51.3,64.5,115.9,64.5,182s-22.9,130.7-64.5,182c-2.8,3.3-6.9,5.1-11,5.1z "+
"M388.7,899.6c0-6.1-5-11.1-11.1-11.1h-138c-6.1,0-11.1,5-11.1,11.1v48.9c0,6.1,5,11.1,11.1,11.1h138c6.1,0,11.1-5,11.1-11.1v-48.9zM636.4,899.6c0-6.1,5-11.1,11.1-11.1h138c6.1,0,11.1,5,11.1,11.1v48.9c0,6.1-5,11.1-11.1,11.1h-138c-6.1,0-11.1-5-11.1-11.1v-48.9z"

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
        dataZoom:[{
            type:"inside",
            xAxisIndex:[0]
        },{
            type:"inside",
            yAxisIndex:[0]
        }],
        legend: {

            // textStyle:{color:"#fff"},
        },
        xAxis: {
            scale: true,
            inverse:true,


        },
        yAxis: {
            scale: true,

        },
        series: [

        ]},
    phaseOpition:{
        animation:false,
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
                symbol: 'none',
                type: 'line',
                stack: 'phase',
                data: []
            },
            {
                name: 'ANT2',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT3',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT4',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT5',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT6',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT7',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT8',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT9',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT10',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT11',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT12',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT13',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT14',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT15',
                type: 'line',
                symbol: 'none',
                stack: 'phase',
                data: []
            },{
                name: 'ANT16',
                type: 'line',
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
        animation:false,
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
                symbol: 'none',
                type: 'line',
                stack: 'rss',
                data: []
            },
            {
                name: 'RSS2',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS3',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS4',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS5',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS6',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS7',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS8',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS9',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS10',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS11',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS12',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS13',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS14',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS15',
                type: 'line',
                symbol: 'none',
                stack: 'rss',
                data: []
            },{
                name: 'RSS16',
                type: 'line',
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
            max:90,
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
            },
            splitNumber:4,


        },
        series: []
    },
    topologyOpition:{
        animation:false,
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
            right:'0',
        },
        tooltip: {},
        animationDurationUpdate: 1500,
        animationEasingUpdate: 'quinticInOut',
        series: [
            {
                type: 'graph',
                layout: 'none',
                symbolSize: 50,
                fixed:true,
                roam: false,
                label: {
                    show: true,
                },
                edgeSymbol: 'circle',
                edgeSymbolSize: [10, 10],
                edgeLabel: {
                    fontSize: 10,
                },
                data: [],
                // links: [],
                links: [],

            }
        ]
    },
    confidenceCdfOpition:{
        title: {
            text: 'Confidence Cdf',
            textStyle:{color:"#fff"},
            left: "center"
        },
        dataZoom:[{
            type:"inside",
            xAxisIndex:[0]
        },{
            type:"inside",
            yAxisIndex:[0]
        }],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross'
            },
        },
        legend: {
            type: 'scroll',
            data: [],
            orient: 'vertical',
            y: 'center',
            x: 'right',
            // textStyle:{color:"#fff"},
        },
        grid: {
            left: '3%',
            right: '15%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
        },
        yAxis: {
            type: 'value'
        },
        series: []
    },
    cdfOpition:{
        title: {
            text: 'CDF',
            textStyle:{color:"#fff"},
            left: "center"
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross'
            },
        },
        dataZoom:[{
            type:"inside",
            xAxisIndex:[0]
        },{
            type:"inside",
            yAxisIndex:[0]
        }],
        grid: {
            left: '3%',
            right: '15%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: [],
            type: 'line',
            smooth: true
        }]
    },
    confidenceBarOpition:{
        tooltip: {
            trigger: 'axis',
        },
        xAxis: {
            type: 'category',
            data: ['confidence1',"confidence2","confidence3"]
        },
        yAxis:  [
            {
                type: 'value',
            },
            {
                type: 'value',
                axisLabel: {
                    formatter: '{value} %'
                }
            }
        ],
        series: [{
            data: [],
            label: {
                show: true
            },
            type: 'bar'
        },{
            type: 'line',
            yAxisIndex: 1,
            data: []
        }]

    },
    routeOpition:{
        title: {
            text: 'Ground Truth Confidence',
            textStyle:{color:"#fff"},
            left: "center"
        },
        dataZoom:[{
            type:"inside",
            xAxisIndex:[0]
        },{
            type:"inside",
            yAxisIndex:[0]
        }],
        tooltip: {},
        //################scatter##############
        legend: {
            type: 'scroll',
            data: ['confidence1','confidence2','confidence3'],
            orient: 'vertical',
            y: 'center',
            x: 'right',
            // selectedMode: false,
            // textStyle:{color:"#fff"},
        },
        xAxis: {
            type:'value'
        },
        yAxis: {
            type:'value'
        },
        series:[{
            type: 'scatter',
            name: 'confidence1',
            data: [],
        },{
            type: 'scatter',
            name: 'confidence2',
            data: [],
        },{
            type: 'scatter',
            name: 'confidence3',
            data: [],
        },
        ]
        //###############heatmap###############
        // xAxis: {
        //     type: 'category',
        //     data: []
        // },
        // yAxis: {
        //     type: 'category',
        //     data: []
        // },
        // visualMap: {
        //     seriesIndex:[0],
        //     min: 1,
        //     max: 3,
        //     calculable: true,
        //     realtime: false,
        //     inRange: {
        //         color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
        //     }
        // },
        // series: [{
        //     name: 'Gaussian',
        //     type: 'heatmap',
        //     data: [],
        //     emphasis: {
        //         itemStyle: {
        //             borderColor: '#333',
        //             borderWidth: 1
        //         }
        //     },
        //     progressive: 1000,
        //     animation: false
        // },
        //     {
        //         type: 'line',
        //         symbol:'none',
        //         symbolSize:0,
        //         data: [],
        //         smooth:true,
        //     },{
        //         type: 'line',
        //         symbol:'none',
        //         symbolSize:0,
        //         data: [],
        //         smooth:true,
        //     }]
    },
    routeErrorOpition:{
        title: {
            text: 'Ground Truth Error',
            textStyle:{color:"#fff"},
            left: "center"
        },
        dataZoom:[{
            type:"inside",
            xAxisIndex:[0],
        },{
            type:"inside",
            yAxisIndex:[0]
        }],
        tooltip: {},
        xAxis: {
            type: 'category',
            data: []
        },
        yAxis: {
            type: 'category',
            data: []
        },
        visualMap: {
            seriesIndex:[0],
            min: 0,
            max: 200,
            calculable: true,
            realtime: false,
            inRange: {
                color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
            }
        },
        series: [{
            name: 'Gaussian',
            type: 'heatmap',
            data: [],
            emphasis: {
                itemStyle: {
                    borderColor: '#333',
                    borderWidth: 1
                }
            },
            progressive: 1000,
            animation: false
        },{
            type: 'line',
            symbol:'none',
            symbolSize:0,
            data: [],
            smooth:true,
        },{
            type: 'line',
            symbol:'none',
            symbolSize:0,
            data: [],
            smooth:true,
        }]
    },
    local3dOpition:{
        xAxis3D: {
            type: 'value',
            min:-200,
            max:200,
            axisLabel: {
                show:false
            },
            axisTick:{
                show:false
            }
        },
        yAxis3D: {
            type: 'value',
            min:-200,
            max:200,
            axisLabel: {
                show:false
            },
            axisTick:{
                show:false
            }
        },
        zAxis3D: {
            type: 'value',
            min:-200,
            max:200,
            axisLabel: {
                show:false
            },
            axisTick:{
                show:false
            }

        },
        grid3D: {
            axisLine: {
                lineStyle: { color: '#fff' }
            },
            axisPointer: {
                lineStyle: { color: '#fff' }
            },
            viewControl: {

            }
        },
        series: [{
            name:'position',
            type: 'scatter3D',
            data: []
        },{
            name:'truth',
            type: 'scatter3D',
            data: []
        }
            ]
    },
    rss:{},
    phase:{},
    rssLine:{},
    aoa:{},
    gatewayChoose:'gateway1',
    queue:'oss.url_test',
    // queue:'replay',
    starImg:"path://M957.111079,403.480424c-3.927449-11.669784-14.447037-19.86442-26.723641-20.816095L647.68068,360.749204,540.183388,84.126003c-4.586458-11.803837-15.951297-19.579941-28.614711-19.579941s-24.02723,7.776104-28.614711,19.579941L375.458719,360.749204l-282.708803,21.915126c-12.276604,0.951675-22.796192,9.146311-26.723641,20.816095-3.927449,11.669784-0.50142,24.557302,8.701173,32.737612l217.547735,193.358823-67.980277,291.298436c-2.848884,12.20702,2.009773,24.919553,12.273535,32.114418,10.264784,7.195889,23.87271,7.42818,34.375925,0.586354l240.624313-156.709111,240.625336,156.709111c5.099135,3.320629,10.92891,4.974291,16.752546,4.974291,6.173606,0,12.342096-1.858324,17.623379-5.561669,10.263761-7.194866,15.122419-19.907399,12.273535-32.114418l-67.980277-291.299459L948.409906,436.218036C957.613522,428.037726,961.037505,415.150208,957.111079,403.480424z",
    atnPic:atnPic,
    signalImg: 'data:img/jpg;base64,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',
    unsignalImg:'data:img/jpg;base64,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',
    atnPos:{},
    atnR:0,
    error:[],
    confidence:{},
    truthError:[],
    truthConfidence:[],
    cdfIndex:[],
    ccdfIndex:[],
    truthArray:[],
    groundTruth:{},
    round:{},
    roundp:[],
    oneMeterRound:[],
    atnRound:[],
    replayLength:1000,
    dayTime:[],
    confidenceTruth:{},
    replay:{
        truth:[],
        position:[],
    },
    // tagList: [],





})
