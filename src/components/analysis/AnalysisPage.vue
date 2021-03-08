<template>
    <div class="analys-container">
        <div>
            <img class="header-blob" src="../../assets/svgs/blob-pink.svg">
            <div class="main-header-font header">Analüüs</div>
        </div>
        <div v-if="!loadingDone" class="upload">
            <p class="lead lead-gray">Muusika faili automaatseks kirjeldamiseks lae meelepärane audiofail üles</p>
            <file-uploader @loadFile="loadFile"/>
            <p class="lead lead-gray">või sisesta YouTube url</p>
            <div class="input-group mb-3">
                <div class="input-group-prepend">
                    <span class="input-group-text" id="inputGroup-sizing-default">
                        <i class="bi bi-globe2"></i>
                    </span>
                </div>
                <input type="text" class="form-control" aria-label="Default"
                       v-model.lazy="url"
                       aria-describedby="inputGroup-sizing-default">
                <div class="input-group-append">
                    <button class="btn btn-outline-secondary" @click="downloadSong" type="button">
                        <i v-if="!searchUrl" class="bi bi-search" ></i>
                        <span v-else class="spinner-border spinner-border-sm"></span></button>
                </div>
            </div>
        </div>
        <div  v-else class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
            <div class="description-header">
                <h4>{{info.nimi}}</h4>
            </div>
            <div class="tempo description">
                <h4><i class="bi bi-speedometer2"></i> {{info.bpm.tempo}} bpm </h4>
                <p class="lead-gray lead">Audio faili tempo on {{info.bpm.tempo}} lööki minutis. {{info.bpm.kirjeldus}} <br> Kuula erinevusi tempode vahel siin.</p>
                <div class="scale">
                    Energia
                    <div class="progress">
                        <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100">25%</div>
                    </div>
                </div>
                <div class="scale">
                    Tantsitavus
                    <div class="progress">
                    <div class="progress-bar" role="progressbar" style="width: 40%;" aria-valuenow="40" aria-valuemin="0" aria-valuemax="100">40%</div>
                </div>
                </div>
            </div>
            <div class="key description">
                <h4><i class="bi bi-music-note-beamed"></i> {{info.helistik.nimi}} </h4>
                <p class="lead-gray lead">{{info.helistik.kirjeldus}}</p>
                <img src="../../assets/images/c-maj.svg" style="width: 20%">
            </div>
            <div class="tags description">
                <h4 class="right-header"><i class="bi bi-tags"></i> Märksõnad </h4>
                <p class="lead-gray lead">Helifaili saab iseloomustada järgnevate märksõnadega:</p>
                <p class="lead-gray lead" v-for="(item, index) in info.taggs" :key="index">
                   <b>{{item.tag}}</b> - {{item.des}}
                </p>
            </div>

        </div>
    </div>
</template>

<script>
    import FileUploader from "../FileUploader";
    import dummy from "../../data/dummyData"
    export default {
        name: "AnalysisPage.vue",
        components: {FileUploader},
        props: [FileUploader],
        data() {
            return {
                loadingDone: false,
                searchUrl: false,
                url:'',
                info: dummy
            }
        },
        methods:{
            downloadSong(){
                this.searchUrl = true;
                console.log(this.url);
                this.loadingDone = true;
            },
            loadFile(file){
                console.log(file);
                this.loadingDone = true;
            }
        }
    }
</script>

<style scoped>
    .analys-container {
        padding: 3rem;
        padding-top: 8%;
    }

    .main-header-font {
        color: darkslategrey;
        font-size: 3rem;
    }

    .header-blob {
        width: 350px;
        margin-top: -100px;
    }

    .header {
        margin-top: -220px;
        margin-left: 45px;
    }

    .upload {
        display: table;
        margin: 0 auto;
        padding-top: 5rem;
    }

.description-header{
    display: flex;
    justify-content:center;
    flex-flow: row nowrap;
    align-items:flex-end;
    gap: 2rem;
}
    .tempo{
        margin-top: 3rem;
        width: 70%;
        margin-left: 0;
    }
p{
    margin-top: -2rem;
}
.description{
    padding-bottom: 3rem;
}
    .key{
        width: 70%;
        margin-right: 0;
        text-align: right;
    }
    .tags{
        width: 70%;
        margin-left: 0;
    }
    .progress-bar{
        background-color: #20bdb2;
    }

.scale{
    padding-bottom: 1rem;
    width: 90%;
}
</style>