<template>
    <div class="loading-container">
        <div class="wrapper">
            <span class="circle circle-1"></span>
            <span class="circle circle-2"></span>
            <span class="circle circle-3"></span>
            <span class="circle circle-4"></span>
            <span class="circle circle-5"></span>
            <span class="circle circle-6"></span>
            <span class="circle circle-7"></span>
            <span class="circle circle-8"></span>
        </div>
        <div class="loading-text">
            Laen andmeid ja kirjeldan
        </div>
    </div>
</template>

<script>
    export default {
        name: "Loading"
    }
</script>

<style scoped>
    /** https://codepen.io/ahmadbassamemran/pen/zQKqba **/
    .loading-container{
        align-items: center;
    }
    .loading-text{
        margin-top: 30%;
        left:50%;
    }
    .wrapper{
        position:absolute;
        top:40%;
        left:50%;
        transform:translate(-50%, -50%);
        width: 250px;
        display: flex;
        justify-content: space-between;
    }
    .circle{
        display: inline-block;
        width: 15px;
        height: 15px;
        background-color: #e79aca;
        border-radius: 50%;
        animation: loading 1.5s cubic-bezier(.8, .5, .2, 1.4) infinite;
        transform-origin: bottom center;
        position: relative;
    }
    @keyframes loading{
        0%{
            transform: translateY(0px);
            background-color: #C71585;
        }
        50%{
            transform: translateY(50px);
            background-color: #20bdb2;
        }
        100%{
            transform: translateY(0px);
            background-color: #b9b1cb;
        }
    }
    .circle-1{
        animation-delay: 0.1s;
    }
    .circle-2{
        animation-delay: 0.2s;
    }
    .circle-3{
        animation-delay: 0.3s;
    }
    .circle-4{
        animation-delay: 0.4s;
    }
    .circle-5{
        animation-delay: 0.5s;
    }
    .circle-6{
        animation-delay: 0.6s;
    }
    .circle-7{
        animation-delay: 0.7s;
    }
    .circle-8{
        animation-delay: 0.8s;
    }



</style>