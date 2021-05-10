const webpack = require("webpack");

module.exports = {
    publicPath:'/',//根路径
    outputDir:'dist',//打包的时候生成的一个文件名
    lintOnSave:true,//是否开启eslint保存检测 ,它的有效值为 true || false || 'error'
    configureWebpack: {
        plugins: [
            new webpack.ProvidePlugin({
                $: 'jquery',
                jQuery: 'jquery',
                'window.jQuery': 'jquery',
                Popper: ['popper.js', 'default'],
            })
        ]
    },

}
