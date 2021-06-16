var express = require('express');
var router = express.Router();
var lrtModel = require('../models/lrtData')
var mongoose = require('../common/mongodb')
var tableDataModel = require('../models/tableData')
const mq = require('../common/mq')
const amqp = require('amqplib/callback_api')


router.get('/', function(req, res, next) {
    let lrtDataModel = mongoose.model('test111',lrtModel)
    let LrtData = new lrtDataModel({
        time: 'req.body.time',
        tagid: 1,
        atnid:1,
        atnpos:[2,2],
        phase: {'gateway1':[1,1,1,1,1,1],'gateway2':[1,1,1,1,1,1]},
        rss: {'gateway1':[1,1,1,1,1,1],'gateway2':[1,1,1,1,1,1]},
        pos: [2,2],
        // rn16:Array,
    })
    LrtData.save(function () {
        res.json({status: 0, message: 'Successful'})
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

       lrtDataModel.findAll(async function (err,data) {
           mq.create(data)
           res.json({
               message:data.length
           })
       })


})


module.exports = router;
