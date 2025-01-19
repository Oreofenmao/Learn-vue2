<template>
  <div class = "loginRegister">
    <div>
    <form @submit.prevent="submitForm">
        <label for="name">
            Name:<input type="text" v-model="name">
        </label>
        <label for="password">
            password:<input type="text" v-model="password">
        </label>
        <br>
        <label for="captcha"> 
            验证码：<input type="text" v-model="captcah">
            <img :src="captchaImageUrl" alt="验证码">
        </label>
        <button type="button" @click="switchPage"> 前往注册界面 </button>
        <button type="submit"> 登录 </button>       
    </form>
    </div>
  </div>
</template>

<script>
export default {
    data() {
    return {
        name: '',  // 注意return
        password: '',
        captcha: '',
        captchaImageUrl: '/captcha/',
        };
    },
    methods:{
        switchPage(){
            this.$emit('changePage','RegisterPage')
        },
        submitForm() {
      // 准备表单数据
      const formData = {
        name: this.name,
        password: this.password,
        captcha: this.captcha
      };

      // 发送 POST 请求到 Django 后端的 /login/ 路由
        this.$axios.post('/login/', formData)
            .then(response => {
                console.log('登录成功', response);  // 登录成功后的操作（如跳转、提示等）
            })
            .catch(error => {
                console.log('登录失败', error.response.data.message);  // 登录失败的错误处理
            });
        }
    }
}
</script>

<style>
    .loginRegister{
        display:flex;
        justify-content: center;
        align-items: center;
        width:auto;
        height:auto;
        border:1px solid red;
    }
    label img{
        margin-top: 10px;
    }
    form{
        display:flex;
        flex-direction: column;
        /* gap:10px; */
    }
    label {
    display: flex;
    flex-direction: column;  /* 使得标签和输入框垂直排列 */
}
    input {
        margin: 5px;  /* 给输入框添加一些间距 */
    }
    button {
        margin: 10px;  /* 给按钮添加一些间距 */
    }
</style>