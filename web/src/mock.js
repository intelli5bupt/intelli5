// /* eslint-disable */
// const Mock = require('mockjs')


// //数据集管理
// let Result ={
//   retCode:200,
//   retMsg:'操作成功',
//   data:null
// }
// var data = [
//     {
//       'deviceIP' : '192.168.33.1',
//       'devicePort': '6031',
//       'datasetName': '数据集一',
//       'datasetAddress': 'D:/program/dataset',
//       'supportBusiness': '某业务',
//       'username': 'admin',
//       'datasetID': '1'
//     },
//     {
//       'deviceIP' : '192.168.33.2',
//       'devicePort': '4508',
//       'datasetName': '数据集二',
//       'datasetAddress': 'E:/program/dataset',
//       'supportBusiness': '某业务',
//       'username': 'admin',
//       'datasetID': '2'
//     }
// ]
// // 数据管理

// // 获取数据
// Mock.mock('data/dataList', 'get', () => {
//   Result.retCode = 200
//   Result.retMsg = '数据获取成功'
//   Result.data  = data
//   return Result
// })

// // 注册数据
// Mock.mock('/data/data_register', 'post', (res) => {
//   console.log('res => ',res)
//   console.log(res.body)
//   Result.retCode = 200
//   Result.retMsg = '添加成功'
//   return Result
// })

// // 删除数据
// Mock.mock('/data/dataDelete?datasetID', 'delete', (res) => {
//   console.log('res => ',res)
//   Result.retCode = 200
//   Result.retMsg = '删除成功'
//   return Result
// })

// // 修改数据
// Mock.mock('/data/dataRetrieve', 'post', (res) => {
//   console.log('res => ',res)
//   Result.retCode = 200
//   Result.retMsg = '修改成功'
//   return Result
// })

// //设备管理
// var data1 = [
//   {
//     'deviceName': "设备1",
//     'deviceIP': "192.168.22.1",
//     'devicePort': "22",
//     'deviceID': '1',
//     'deviceStatus': "在线",
//   },
//   {
//     'deviceName': "设备2",
//     'deviceIP': "192.168.23.1",
//     'devicePort': "44",
//     'deviceID': '2',
//     'deviceStatus': "离线",
//   },
//   {
//     'deviceName': "设备3",
//     'deviceIP': "192.168.32.1",
//     'devicePort': "22",
//     'deviceID': '3',
//     'deviceStatus': "在线",
//   },
  

// ]

// // 获取设备列表
// Mock.mock('/device/deviceRetrieve', 'get', () => {
// Result.retCode = 200
// Result.retMsg = '设备列表获取成功'
// Result.data  = data1
// return Result
// })

// // 注册设备
// Mock.mock('/device/deviceCreate', 'post', (res) => {
// console.log('res => ',res)
// console.log(res.body)
// Result.retCode = 200
// Result.retMsg = '设备添加成功'
// return Result
// })

// // 删除设备
// Mock.mock('/device/deviceDelete?deviceID', 'delete', (res) => {
// console.log('res => ',res)
// Result.retCode = 200
// Result.retMsg = '删除成功'
// return Result
// })

// // 修改设备
// Mock.mock('/device/deviceUpdate', 'post', (res) => {
// console.log('res => ',res)
// Result.retCode = 200
// Result.retMsg = '修改成功'
// return Result
// })


// //业务创建
