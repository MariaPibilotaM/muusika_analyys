<template>
    <div style="overflow: hidden">
        <div class="wave landing">
            <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
                <main class="main-landing">
                    <div class="banner lead">
                        <div class="card-title">
                            <div class="logo">
                                <img src="../../assets/images/logo_white_wo_text.png">
                            </div>
                            <div class="main-header-font">Muusik</div>
                        </div>
                        <div>
                            Nutikas abimees meloodilistes küsimustes.
                        </div>
                    </div>
                </main>
            </div>
        </div>
        <Introduction class="introduction"></Introduction>
        <div class="blob-as-bg left" style="width: 600px; height: 400px">
            <img class="blob-pink" src="../../assets/svgs/blob (1).svg">
        </div>
        <div class="left-section">
            <div>
                <div class="upload-header lead custom-lead"> Analüüsi meelepärast muusikapala
                </div>
            </div>
            <div class="description">
                <p class="lead-gray">Oled alati mõelnud, mis on muusika edetabeleid vallutava laulu valem? Nüüd saad
                    vaid sekunditega analüüsida oma lemmik YouTube platvormil leiduvat hittlugu. Vali välja meelepärane
                    jazz, kantri või hoopis R&B teos, sisesta veebilink ja avasta tõeline muusik enda sees. </p>
                <div class="navigation">
                    <router-link to="/kirjelda">Proovi kohe SIIN!</router-link>
                </div>
            </div>
        </div>
        <div class="blob-as-bg right" style="width: 600px; height: 400px">
            <img class="blob-green" src="../../assets/svgs/blob_green.svg">
        </div>
        <div class="right-section">
            <div>
                <p class="lead-gray">Ei oska kuidagi omaloomingut kirjeldada, sest oled avastanud uudse hübriid žanri?
                    Lae üles muusikapala ning saa põhjalik ülevaade alustades märksõnadest, lõpetades tempomuutuste ja
                    kulminatsiooniga.</p>
                <div class="navigation">
                    <router-link to="/kirjelda">Uuri lisa SIIN!</router-link>
                </div>
            </div>
            <div>
                <div class="upload-header lead custom-lead"> Lae üles enda teos
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import Introduction from "./Introduction";

    export default {
        name: 'LandingPage',
        components: {
            Introduction,
        },
        data() {
            return {
                show: false
            }
        }
    }
</script>

<style lang="scss">
    /*
 * Back-grounds
 */
    .landing {
        text-shadow: 0 .05rem .1rem rgba(0, 0, 0, .5);
        box-shadow: inset 0 0 5rem rgba(0, 0, 0, .5);
    }

    .blob-green {
        margin-top: -270px;
    }

    .right {
        float: right;
        margin-right: 3rem;
    }

    .blob-pink {
        margin-top: -100px;
        width: 700px;
    }

    .blob-as-bg {
        position: relative;
        text-align: center;
        color: white;
    }

    .introduction {
        padding-top: 3rem;
        padding-right: 6rem;
        padding-left: 6rem;
    }

    .card-title {
        display: flex;
        flex-flow: row nowrap;
        gap: 1rem;
        align-items: flex-end;
    }

    .main-landing {
        margin-top: 4rem;
    }

    .main-header-font {
        display: flex !important;

    }

    .upload-header {
        font-size: 55px;
        padding: 15px;
        height: 300px;
        color: #000000;
        text-align: center;
    }

    .left-section {
        display: grid;
        grid-template-columns: 650px auto;
        grid-gap: 50px;
        padding-bottom: 3rem;
        margin-top: -130px;
        margin-left: 90px;
    }

    .right-section {
        display: grid;
        grid-template-columns: 100% 450px;
        grid-gap: 50px;
        padding-bottom: 3rem;
        margin-left: 90px;
        margin-top: -50px;
    }

    .centered {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    .description {
        display: block;
        margin-left: auto;
        margin-right: 3rem;
    }

    .custom-lead {
        line-height: 1.0;
    }

    .banner {
        text-align: right !important;
        margin-right: 6rem;
    }
</style>
