var express = require('express');
var router = express.Router();
var lrtModel = require('../models/lrtdata')
var mongoose = require('../common/mongodb')
var tableDataModel = require('../models/tableData')

router.get('/', function(req, res, next) {
    res.send('respond with a resource');
});
router.post('/insert', function(req, res, next) {
    let lrtDataModel = mongoose.model(req.body.table,lrtModel)
    let LrtData = new lrtDataModel({
        time: req.body.time,
        tagid: req.body.tagid,
        atnid:req.body.atnid,
        phase: req.body.phase,
        rss: req.body.rss,
        pos: req.body.pos,
        // rn16:Array,
    })
    LrtData.save(function () {
        res.json({status: 0, message: 'Successful'})
    })

});
router.post('/insertTable', function(req, res, next) {
    let tableData = new tableDataModel({
        antPos:req.body.antPos,
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


module.exports = router;
