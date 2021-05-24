import * as math from 'mathjs'
import {state} from "../store/state";
const sortArr = [3,2,1,4,7,6,5,8]

function computeAtan(){
    let atanArr = []
    for(let i = 0;i<8;i++){
        let midNum = math.atan(state.antPos[i][1]/state.antPos[i][0])
        atanArr.push(printFn(midNum))
    }
    return atanArr
}
function computeR(){
    let rArr = []
    for(let i = 0;i<8;i++){
        let midNum = math.sqrt(math.pow(state.antPos[i][1],2)+math.pow(state.antPos[i][0],2))
        rArr.push(printFn(midNum))
    }
    return rArr
}
function computeIndex(alpha,beta,phi,theta,r){
    return theta+(2*Math.PI*r/0.32)*math.cos(alpha-phi)*math.cos(beta)
}

function ten_two(c_Value){
    var two=parseInt(c_Value,16).toString(2);
    var Point=[];
    if(two.length<8){
        for(var j=0;j<(8-two.length);j++){
            Point.push('0')
        }
    }
    for(var k=0;k<two.length;k++){
        Point.push(two.charAt(k))

    }
    return Point;

}
function binary2angle(a,b){
        if(a==='0'){
            if(b==='0'){
                return 0.75*Math.PI
            }else {
                return 0
            }
        }else{
            if(b==='0'){
                return 0.25*Math.PI
            }else {
                return 0.5*Math.PI
            }
        }
}

function printFn(value) {
    const precision = 3
    return Number(math.format(value, precision))
}

function convPhase(Phase0,PhaseA,PhaseB){
    let midPhase = []
    let a = ten_two(PhaseA)
    let b = ten_two(PhaseB)
    let o = (Phase0/64)*2*Math.PI
    for(let i = 0 ;i<8;i+=2){
        midPhase.push(printFn(binary2angle(a[i],a[i+1])+o))
    }
    for(let i = 0 ;i<8;i+=2){
        midPhase.push(printFn(binary2angle(b[i],b[i+1])))
    }
    let phase = []
    sortArr.forEach((v)=>{
        phase.push(midPhase[v-1])
    })
    console.log(phase)
    return phase
}

function compSpectrum(Phase0,PhaseA,PhaseB){
    let spectrumArray = []
    let phase = convPhase(Phase0,PhaseA,PhaseB)
    let phi = computeAtan()
    let r = computeR()
    for (let i= 0;i<360;i++){
        for(let j = 0;j<90;j++){
            let cosIndex = 0
            let sinIndex = 0
            for (let k =0;k<8;k++){
                let a = computeIndex(i,j,phi[k],phase[k],r[k])
                cosIndex += math.cos(a)
                sinIndex += math.sin(a)
            }
            let res = printFn(math.sqrt(math.pow(cosIndex,2)+math.pow(sinIndex,2))/8)
            spectrumArray.push([i,j,res])
        }
    }

    return spectrumArray

}
export {
    compSpectrum,convPhase
}
