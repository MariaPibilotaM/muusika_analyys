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
                Tempo muutuste ja kulminatsiooni kirjeldused aitavad tõeliselt mõista muusikapala hingeelu. Lisaks pakuvad audio nii tempoterminid kui ka tantsitavuse ja energia tase olulist lisaväärtust muusika huvilisele.
            </p></div>
        <div class="feature-description">
            <img src="../../assets/images/tempo_gray.png">
            <p class="lead lead-gray">
                Jazz, rokk, funk või hoopis house? Nutikas abimees oskab valida ligi 50 erineva märksõna vahel sobivaima ja annab ülevaate žanri eripäradest.
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