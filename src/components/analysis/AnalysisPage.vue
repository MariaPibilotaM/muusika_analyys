<template>
    <div class="header-container">
        <div v-if="!loadingScreen">
            <img class="header-blob" src="../../assets/svgs/blob-pink.svg">
            <div class="main-header-font-gray header">Analüüs</div>
        </div>
        <div v-if="!loadingDone && !loadingScreen" class="upload">
            <Upload @addData="addData" @addFile="addFile"></Upload>
        </div>
        <div v-if="loadingScreen" class="loading-animation">
        <Loading></Loading>
        </div>
    </div>
</template>

<script>
    import Upload from "./Upload";
    import Loading from "./Loading";
    //import dummy from "../../data/dummyData"
    import MusicDescription from "./MusicDescription";
    import axios from "axios";

    export default {
        name: "AnalysisPage.vue",
        components: { Upload, Loading},
        props: [MusicDescription],
        data() {
            return {
                loadingDone: false,
                searchUrl: false,
                url: '',
                info: {},
                loadingScreen: false,
            }
        },
        methods: {
            addFile(file){
                this.loadingScreen = true;
                const path = 'http://prog.keeleressursid.ee/veebid/muusika_analyys/data';
                axios.delete(path)
                    .catch((error) => {
                        console.error(error);
                    });
                let params = new FormData();
                params.append('file', file.file);
                params.append('link', '-');
                axios.post(path, params)
                    .then(() => {
                        this.$router.push({ name: 'Tulemus' })
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            },
            addData(url) {
                this.loadingScreen = true;
                const path = 'http://prog.keeleressursid.ee/veebid/muusika_analyys/data';
                axios.delete(path)
                    .catch((error) => {
                        // eslint-disable-next-lined
                        console.error(error);
                    });
                let params = new FormData();
                params.append('link', url)

                axios.post(path, params)
                    .then(() => {
                        this.$router.push({ name: 'Tulemus' })
                    })
                    .catch((error) => {
                        console.log(error);
                    });
            },
        },
    }
</script>

<style scoped>

    .loading-animation {
        display: table;
        margin: 0 auto;
        padding: 5rem;
    }

</style>