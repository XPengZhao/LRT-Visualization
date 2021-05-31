var mongoose = require('../common/mongodb')

var lrtData = new mongoose.Schema({
    tagId:String,
    logTime:String,
    phyTime:String,
    savedTime:String,
    position: Array,
    truth:Array,
    xServer: Array,
    spectrum:Array,
    // rn16:Array,
})

lrtData.statics.findTag = function (tagid, callback){
    this.find({tagid:tagid},callback)
}
lrtData.statics.findTagandTimeStamp = function (tagid, timestamp, callback){
    this.find({tagid:tagid,TimeStamp:timestamp},callback)
}
lrtData.statics.findAll = function (callback) {
    this.find({},callback)
}


module.exports = lrtData
