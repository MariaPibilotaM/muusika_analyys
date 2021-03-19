<template>
    <div class="description-grid">
        <div class="feature-description">
            <img src="../../assets/images/sound_gray.png">
            <p class="lead lead-gray">
                Vali välja meelepärane pala, lae üles või esita YouTube veebilingina ning avasta rohkem! Rakendus Muusik
                pakub laialdase analüüsi ja kirjelduse eesti keeles. Rakendus on abiline meloodilistes
                küsimustes, sest meie usume, et igaüks on muusik.
            </p>
        </div>
        <div class="feature-description">
            <img src="../../assets/images/dance_gray.png">
            <p class="lead lead-gray">
                Muusikapala hingeelu tõelislt mõistmiseks ei piisa ainult helistikust ja esitamise tempost.
                Veebirakendus Muusik aitab mõista detaile, mis muidu jääksid märkamata. Tempoterminid, kulminatsioon ja
                muutused esitamise kiiruses on olulised iseloomujooned nii J. S. Bach suurvormis kui ka Liis Lemsalu
                tantsuhitis.</p></div>
        <div class="feature-description">
            <img src="../../assets/images/tempo_gray.png">
            <p class="lead lead-gray">
                Jazz, rokk, funk või hoopis house? Nutikas abimees oskab valida ligi 50 erineva märksõna vahel. Žanri
                eripärad ja tagg-sõnade unikaalsed kooslused aitavad esile tuua muusikateose eripärad.
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
        grid-gap: 6rem;
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