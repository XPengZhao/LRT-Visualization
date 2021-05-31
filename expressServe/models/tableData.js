var mongoose = require('../common/mongodb')

var tabledata = new mongoose.Schema({
    Describe:String,
    img: String,
    tableName: String
})

tabledata.statics.findAll = function (id,callback){
    this.find({},callback)
}
tabledata.statics.deleteTable = function (tableName,callback){
    this.remove({tableName:tableName},callback)
}

var tableDataModle = mongoose.model('tabledata',tabledata)
module.exports = tableDataModle

