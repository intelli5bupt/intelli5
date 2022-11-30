const path = require('path')
const resolve = dir => {
  return path.join(__dirname, dir)
}
module.exports = {
  // open: true,
  // publicPath: './',
  // chainWebpack: config => {
  //   config.resolve.alias
  //     .set('_c', resolve('src/components')) // key,value自行定义，比如.set('@@', resolve('src/components'))
  // },
  devServer: {
    // proxy: 'http://10.128.133.23:8081' 这种写法也可以

    proxy: {

      '/api/steel': {
        target: 'http://10.112.76.172:43999',
        changeOrigin: true,
        pathRewrite:{
          '^/api/steel': '/api/steel'
        }
      },
      
      '/api': {
        target: 'http://10.128.133.23:8081',
        changeOrigin: true,
        pathRewrite:{
          '^/api': '/api'
        }
      }
      

    
    }
    
  }
  
  
}
