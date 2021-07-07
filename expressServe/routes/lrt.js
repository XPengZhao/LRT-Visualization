var express = require('express');
var router = express.Router();
var lrtModel = require('../models/lrtData')
var mongoose = require('../common/mongodb')
var tableDataModel = require('../models/tableData')
const mq = require('../common/mq')
const cdf = require('cumulative-distribution-function');

function  distanceCompute(x1,x2,y1,y2){
    let a = Math.pow((x1-x2),2)
    let b = Math.pow((y1-y2),2)
    return Number(Math.sqrt(a+b).toFixed(2))*100
}

function locate(gt) {
    let x1 = gt['gateway1'][0]
    let y1 = gt['gateway1'][1]
    let x2 = gt['gateway2'][0]
    let y2 = gt['gateway2'][1]
    let x3 = gt['gateway3'][0]
    let y3 = gt['gateway3'][1]
    var a, b;
    a = (y2 - y1) / (x2 - x1);
    b = y1 - a * x1;

    var xMiddle = (x1 + x2) / 2;
    var yMiddle = (y1 + y2) / 2;
    var c, lastX, lastY;
    if (a != 0) {
        c = yMiddle - (-1 / a) * xMiddle;
        lastX = (Math.pow(x1, 2) + Math.pow(y1, 2) - Math.pow(x3, 2) - Math.pow(y3, 2) - 2 * c * y1 + 2 * c * y3) / (2 * ((x1 - x3) - (1 / a) * (y1 - y3)));
        lastY = (-1 / a) * lastX + c;
    } else {
        lastX = c = xMiddle;
        lastY = (Math.pow(x1, 2) + Math.pow(y1, 2) - Math.pow(x3, 2) - Math.pow(y3, 2) + 2 * lastX * (x3 - x1)) / (2 * (y1 - y3));
    }
    let r = Number(Math.sqrt(Math.pow(lastX-x1,2)+Math.pow(lastY-y1,2)).toFixed(2))
    return {x:parseInt(lastX),y:parseInt(lastY),r:parseInt(r)}
}

function comp8p(x,y,r,truthMinX,truthMinY) {
    let roundp = []
    for(let i = 0;i<360;i++){
        let hudu = 2*Math.PI/360*i
        let x1 = x + Math.sin(hudu)*r
        let y1 = y - Math.cos(hudu)*r
        roundp.push([x1,y1])
    }
    roundp = roundp.map(function (num) {
        return[num[0]+Math.abs(truthMinX),num[1]+Math.abs(truthMinY)]
    })
    return roundp

}



router.get('/', function(req, res, next) {
    let lrtDataModel = mongoose.model('2021/7/2 01:17:16',lrtModel)
    lrtDataModel.findAll(function (err,data) {
        mq.create(data)
        res.json({
            message:'success'
        })
    })
});
router.post('/insert', function(req, res, next) {
    let lrtDataModel = mongoose.model(req.body.table,lrtModel)
    let LrtData = new lrtDataModel({
        tagId:req.body.tagId,
        logTime:req.body.logTime,
        phyTime:req.body.phyTime,
        savedTime:req.body.savedTime,
        position: req.body.position,
        truth:req.body.truth,
        xServer: req.body.xServer,
        spectrum:req.body.spectrum,
        // rn16:Array,
    })
    LrtData.save(function () {
        res.json({status: 0, message: 'Successful'})
    })

});
router.post('/insertTable', function(req, res, next) {
    let tableData = new tableDataModel({
        Describe:req.body.Describe,
        img: req.body.img,
        tableName: req.body.tableName
    })

    tableData.save(function () {
        res.json({status: 0, message: 'Successful'})
    })

});

router.post('/searchData',function (req,res,next){
    tableDataModel.findAll(1,function (err,data){
        res.send(data)
    })
})
router.post('/deleteTable',function (req,res,next){
    mongoose.connection.db.dropCollection(req.body.tableName, function(err, result) {
        if(!err){
            console.log('success')
        }else {
            console.log(err)
        }
    });
    tableDataModel.deleteTable(req.body.tableName,function (err,data){
        if(err){
            console.log(err)
        } else {
            res.json({
                message:'success'
            })
        }

    })

})
router.post('/replay',function (req,res,next){
    let lrtDataModel = mongoose.model(req.body.table,lrtModel)
    let position = []
    let truth = []
       lrtDataModel.findAll(async function (err,data) {
           for(let i = 0;i<data.length;i++){
               position.push(data[i].position)
               truth.push(data[i].truth)
           }
           let xRange=data[0].spectrum[0].xRange
           let zRange=data[0].spectrum[0].xRange
           res.json({
               len:data.length,
               message:{
                   position:position,
                   truth:truth,
                   xRange:xRange,
                   zRange:zRange
               }
           })
       })


})
router.post('/analysis',function (req,res,next) {
    let lrtDataModel = mongoose.model(req.body.table,lrtModel)
    var errorNumArray = []
    var truthError = []
    var truthConfidence = []
    var confidence = []
    var truthMaxX = 0
    var truthMinX = 0
    var truthMaxY = 0
    var truthMinY = 0
    var truthArray = []
    var groundTruth = {}
    lrtDataModel.findAll(async function (err,data) {
        for(let i = 0;i<data.length;i++){
            for(let key in data[i].xServer[0].gateways){
                if(!groundTruth[key]){
                    if(data[i].xServer[0].gateways[key].position[0][2]){
                        groundTruth[key]=[parseInt(data[i].xServer[0].gateways[key].position[0][0].toFixed(2)*100),parseInt(data[i].xServer[0].gateways[key].position[0][2].toFixed(2))*100]
                    }else {
                        groundTruth[key]=[parseInt(data[i].xServer[0].gateways[key].position[0].toFixed(2)*100),parseInt(data[i].xServer[0].gateways[key].position[1].toFixed(2))*100]
                    }

                }
            }

            let errorNum=distanceCompute(data[i].truth[0],data[i].position[0],data[i].truth[2],data[i].position[2])
            errorNumArray.push(errorNum)
            let truthX = parseInt(Number(data[i].truth[0].toFixed(2))*100)
            let truthY = parseInt(Number(data[i].truth[2].toFixed(2))*100)
            if(data[i].spectrum[0].confidence in confidence){
                confidence[data[i].spectrum[0].confidence].push(errorNum)
            }else {
                confidence[data[i].spectrum[0].confidence] = [errorNum]
            }

            // if(truthX>truthMaxX){
            //     truthMaxX = truthX
            // }
            // if(truthY>truthMaxY){
            //     truthMaxY = truthY
            // }
            // if(truthX<truthMinX){
            //     truthMinX = truthX
            // }
            // if(truthY<truthMinY){
            //     truthMinY = truthY
            // }

            truthArray.push([truthX,truthY])
            truthError.push([truthX,truthY,errorNum])
            truthConfidence.push([truthX,truthY,data[i].spectrum[0].confidence])
        }
        let ccdfIndex = {}
        for(let key in confidence){
            let ccdf = cdf(confidence[key])
            let y = ccdf.ps()
            let ccdfy = y.map(function (num) {
                return Number(num.toFixed(3))
            })
            for(let i=0;i<ccdfy.length;i++) {
                if (0.65< ccdfy[i] && ccdfy[i] < 0.7) {
                    if (ccdfIndex[key]) {
                        ccdfIndex[key].push(i)
                    } else {
                        ccdfIndex[key] = [i]
                    }
                }
            }
        }

        let index = []
        let mycdf = cdf(errorNumArray)
        let cdfIndex = mycdf.ps()
        let cdfy = cdfIndex.map(function (num) {
            return Number(num.toFixed(3))
        })
        for(let i=0;i<cdfy.length;i++){
            if(0.65<cdfy[i] && cdfy[i]<0.7){
                index.push(i)
            }
        }
        let round = locate(groundTruth)
        truthMaxX=round.x+round.r
        truthMaxY=round.y+round.r
        truthMinX=round.x-round.r
        truthMinY=round.y-round.r
        truthConfidence = truthConfidence.map(function (num) {
            return[num[0]+Math.abs(truthMinX),num[1]+Math.abs(truthMinY),num[2]]
        })
        truthError = truthError.map(function (num) {
            return[num[0]+Math.abs(truthMinX),num[1]+Math.abs(truthMinY),num[2]]
        })
        for(let key in groundTruth){
            groundTruth[key][0] += Math.abs(truthMinX)
            groundTruth[key][1] += Math.abs(truthMinY)
        }
        let roundp = comp8p(round.x,round.y,round.r,truthMinX,truthMinY)
        let roundr1 = comp8p(round.x,round.y,100,truthMinX,truthMinY)

        res.json({
            error:errorNumArray,
            confidence:confidence,
            truthError:truthError,
            truthConfidence:truthConfidence,
            index:index,
            ccdfIndex:ccdfIndex,
            truthMaxX:round.x+round.r,
            truthMaxY:round.y+round.r,
            truthMinX:round.x-round.r,
            truthMinY:round.y-round.r,
            truthArray:truthArray,
            groundTruth:groundTruth,
            round:round,
            roundp:roundp,
            roundr1:roundr1
        })
    })
})


module.exports = router;
