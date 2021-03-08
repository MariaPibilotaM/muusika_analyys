<template>
    <div class="description-grid">
        <div class="feature-description">
            <img src="../../assets/images/sound_gray.png">
            <p class="lead lead-gray">
                Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer
            </p>
        </div>
        <div class="feature-description">
            <img src="../../assets/images/dance_gray.png">
            <p class="lead lead-gray">
                Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer
            </p></div>
        <div class="feature-description">
            <img src="../../assets/images/tempo_gray.png">
            <p class="lead lead-gray">
                Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer
            </p></div>

    </div>
</template>

<script>
    export default {
        name: "Introduction"
    }
</script>

<style scoped>
    .description-grid {
        display: grid;
        grid-template-columns: auto auto auto;
        grid-gap: 50px;
        padding-bottom: 5rem;
    }


    img {
        width: 90px;
        height: 90px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    .feature-description {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

</style>