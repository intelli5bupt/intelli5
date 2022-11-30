import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import dataV from '@jiaminghi/data-view';
import Element from 'element-ui'
import "element-ui/lib/theme-chalk/index.css"
import axios from 'axios'
// import store from './store'



// var axios1 = require('axios')
// axios.defaults.baseURL = '/http://10.128.133.23:8081/api';
axios.defaults.baseURL = '/api';

axios.defaults.withCredentials=true;
Vue.prototype.$axios = axios;

// module.exports = {
//   dev: {
//     proxyTable: {
//       '/api': {
//         target: 'http://10.128.133.23:8081/api',
//         chainOrigin: true,
//           '^api': ''
//       }
//     }
//   }
// }

Vue.use(Element)
Vue.use(dataV);


// var axios = require('axios')
// axios.defaults.baseURL = 'http://10.128.133.23:8080/'
// // 全局注册，之后可在其他组件中通过 this.$axios 发送数据
// Vue.prototype.$axios = axios
// Vue.config.productionTip = false

// 按需引入vue-awesome图标
import Icon from 'vue-awesome/components/Icon';
import 'vue-awesome/icons/chart-bar.js';
import 'vue-awesome/icons/chart-area.js';
import 'vue-awesome/icons/chart-pie.js';
import 'vue-awesome/icons/chart-line.js';
import 'vue-awesome/icons/align-left.js';

// 全局注册图标
Vue.component('icon', Icon);
// require("./mock.js")  //引入mock数据，关闭则注释该行
// 适配flex
import '@/common/flexible.js';

// 引入全局css
import './assets/scss/style.scss';


//引入echart
import echarts from 'echarts'
Vue.prototype.$echarts = echarts

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
