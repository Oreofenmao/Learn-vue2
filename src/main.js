import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

Vue.config.productionTip = false

Vue.prototype.$axios = axios;  // 将 axios 挂载到 Vue 实例上，方便全局调用
axios.defaults.baseURL = 'http://127.0.0.1:8000/';  // 设置 Django 后端的基础 URL
new Vue({
  router,
  store,
  axios,
  render: h => h(App)
}).$mount('#app')
