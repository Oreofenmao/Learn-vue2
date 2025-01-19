<template>
  <div id="app">
    <mainLayout></mainLayout>
  </div>
</template>
<script>
import mainLayout from './views/mainLayout.vue'
export default {
  name: 'App',
  components: {
    mainLayout
  }
};
</script>

<style>
  html,body{
    box-sizing: border-box;
    margin:0;
    padding:0;
    width:100%;
    height:100%;
    border: 1px solid red;
  }
</style>
