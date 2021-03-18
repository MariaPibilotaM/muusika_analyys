<template>
    <div class="upload">
        <div class="file-container">
            <p class="lead lead-gray">Muusika automaatseks kirjeldamiseks lae üles meelepärane audiofail</p>
            <file-uploader @loadFile="loadFile"/>
        </div>
        <p class="lead lead-gray">või sisesta YouTube veebilink</p>
        <div class="input-group mb-3">
            <div class="input-group-prepend" >
                    <span class="input-group-text" id="inputGroup-sizing-default">
                        <i class="bi bi-globe2"></i>
                    </span>
            </div>
            <input type="text" class="form-control" aria-label="Default"
                   v-model.lazy="url"
                   aria-describedby="inputGroup-sizing-default"
                   v-on:keyup.enter="addData">
            <div class="input-group-append">
                <button class="btn btn-outline-secondary" @click="addData" type="button">
                    <i class="bi bi-search"></i>
                </button>
            </div>
        </div>
    </div>
</template>

<script>
    import FileUploader from "../FileUploader";

    export default {
        name: "Upload",
        components: {FileUploader},
        props: [],
        data() {
            return {
                url: '',
            }
        },
        methods: {
            loadFile(file) {
                this.$emit("addFile", file[0]);
            },
            addData() {
                this.$emit("addData", this.url);
            },
        },
    }
</script>

<style scoped>
    .upload {
        display: table;
        margin: 0 auto;
        padding-top: 1rem;
    }

    p {
        margin-top: -2rem;
    }

    .file-container {
        padding-bottom: 3rem;
    }
</style>