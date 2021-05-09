var mongoose = require('../common/mongodb')

var lrtdata = new mongoose.Schema({
    time: String,
    tagid: Number,
    atnid: Number,
    phase: Array,
    rss: Array,
    pos: Array,
    // rn16:Array,
})

lrtdata.statics.findTag = function (tagid, callback){
    this.find({tagid:tagid},callback)
}
lrtdata.statics.findTagandTimeStamp = function (tagid,timestamp, callback){
    this.find({tagid:tagid,TimeStamp:timestamp},callback)
}


module.exports = lrtdata
