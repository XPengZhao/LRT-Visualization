var mongoose = require('../common/mongodb')

var lrtData = new mongoose.Schema({
    time: String,
    tagid: Number,
    atnid: Number,
    atnpos:Array,
    phase: Array,
    rss: Array,
    pos: Array,
    // rn16:Array,
})

lrtData.statics.findTag = function (tagid, callback){
    this.find({tagid:tagid},callback)
}
lrtData.statics.findTagandTimeStamp = function (tagid, timestamp, callback){
    this.find({tagid:tagid,TimeStamp:timestamp},callback)
}


module.exports = lrtData
