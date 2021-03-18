<template>
    <div id="page-container">
        <div id="content-wrap">
            <Navbar class="menu"></Navbar>
            <router-view></router-view>
        </div>
        <div style="overflow: hidden; height: 230px" id="footer">
            <img src="./assets/svgs/wave-purple.svg">
        </div>
    </div>
</template>
<script>
    import Navbar from "./components/Navbar";
    export default {
        components: {
            Navbar,
        },
        data(){
            return{
                show:false
            }
        }
    }
</script>
<style lang="scss">
    @import './assets/style/custom.scss';
    @import '../node_modules/bootstrap/scss/bootstrap.scss';
    @import url('https://fonts.googleapis.com/css2?family=Warnes&display=swap');
    @import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.4.0/font/bootstrap-icons.css");
    @import "~vue-file-agent/dist/vue-file-agent.css";

.menu{
    z-index: 999999 !important;
}
</style>
