var mongoose = require('../common/mongodb')

var tabledata = new mongoose.Schema({
    antPos:Array,
    Describe:String,
    img: String,
    tablename: String
})
tableDataModle = mongoose.model('tableData',tabledata)
module.exports = tableDataModle
