var mongoose = require('mongoose')
var url = 'mongodb://tagsys:tagsys@158.132.255.205:27017/LRT?authSource=admin&w=1'
mongoose.connect(url,{useNewUrlParser: true, useUnifiedTopology: true })

module.exports = mongoose
