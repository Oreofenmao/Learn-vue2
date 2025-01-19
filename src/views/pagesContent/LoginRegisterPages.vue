<template>
    <component :is="changePage" @changePage="handleChangePage"/>
</template>

<script>
import LoginPage from '@/components/LoginPage.vue';
import RegisterPage from '@/components/RegisterPage.vue';
export default {
    name:"LoginRegisterPages",
    data(){
        return{
            changePage:'LoginPage',
        }
    },
    methods:{
        handleChangePage(page){
            this.changePage = page;
            console.log(this.changePage);
        }
    },
    components:{
        LoginPage,
        RegisterPage,
    }

}
</script>

<style>

</style>