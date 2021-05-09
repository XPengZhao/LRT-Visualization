var express = require('express');
var router = express.Router();
var lrtModel = require('../models/lrtdata')
var mongoose = require('../common/mongodb')
var tableDataModel = require('../models/tableData')

/* GET users listing. */
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
    console.log(req.body.tableName)
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


module.exports = router;
