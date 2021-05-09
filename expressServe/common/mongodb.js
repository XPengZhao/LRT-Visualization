var mongoose = require('mongoose')
var url = 'mongodb://localhost:27017/LRT'
mongoose.connect(url)

module.exports = mongoose
