<template>
    <div class="mainLayout">
      <login-register-pages></login-register-pages>
    </div>
  </template>
  
  <script>
import LoginRegisterPages from './pagesContent/LoginRegisterPages.vue';
  export default {
    name: 'mainLayout',
    components: {
      LoginRegisterPages,
    }
  };
  </script>
  
  <style scoped>
  .mainLayout{
    display: flex;
    justify-content: center;
    align-items: center;
  }
  </style>
  