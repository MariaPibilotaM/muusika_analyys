<template>
    <div>
        <VueFileAgent
                ref="vueFileAgent"
                :theme="'list'"
                :multiple="true"
                :deletable="true"
                :meta="true"
                :accept="'audio/*'"
                :maxSize="'30MB'"
                :maxFiles="1"
                :helpText="'Lohista helifail või vajuta siia'"
                :errorText="{
      type: 'Vale faili tüüp! Lubatud on ainult muusikafailid.',
      size: 'Liiga suur fail!',
    }"
                @select="filesSelected($event)"
                @beforedelete="onBeforeDelete($event)"
                @delete="fileDeleted($event)"
                v-model="fileRecords"
        ></VueFileAgent>
        <button class="btn btn-outline-secondary float-right" v-if="fileRecords.length > 0" type="button"
                @click="$emit('loadFile',fileRecords)">Kirjelda
        </button>
    </div>
</template>

<script>
    export default {
        name: "FileUploader",
        data: function () {
            return {
                fileRecords: [],
                uploadUrl: 'https://www.mocky.io/v2/5d4fb20b3000005c111099e3',
                uploadHeaders: {'X-Test-Header': 'vue-file-agent'},
                fileRecordsForUpload: [], // maintain an upload queue
            }
        },
        methods: {
            uploadFiles: function () {
                // Using the default uploader. You may use another uploader instead.
                // this.$refs.vueFileAgent.upload(this.uploadUrl, this.uploadHeaders, this.fileRecordsForUpload);
                console.log(this.fileRecordsForUpload)
            },
            deleteUploadedFile: function (fileRecord) {
                // Using the default uploader. You may use another uploader instead.
                this.$refs.vueFileAgent.deleteUpload(this.uploadUrl, this.uploadHeaders, fileRecord);
            },
            filesSelected: function (fileRecordsNewlySelected) {
                var validFileRecords = fileRecordsNewlySelected.filter((fileRecord) => !fileRecord.error);
                this.fileRecordsForUpload = this.fileRecordsForUpload.concat(validFileRecords);
            },
            onBeforeDelete: function (fileRecord) {
                var i = this.fileRecordsForUpload.indexOf(fileRecord);
                if (i !== -1) {
                    // queued file, not yet uploaded. Just remove from the arrays
                    this.fileRecordsForUpload.splice(i, 1);
                    var k = this.fileRecords.indexOf(fileRecord);
                    if (k !== -1) this.fileRecords.splice(k, 1);
                } else {
                    if (confirm('Are you sure you want to delete?')) {
                        this.$refs.vueFileAgent.deleteFileRecord(fileRecord); // will trigger 'delete' event
                    }
                }
            },
            fileDeleted: function (fileRecord) {
                var i = this.fileRecordsForUpload.indexOf(fileRecord);
                if (i !== -1) {
                    this.fileRecordsForUpload.splice(i, 1);
                } else {
                    this.deleteUploadedFile(fileRecord);
                }
            },
        }
    }
</script>

<style scoped>
    .btn {
        margin-top: 15px;
    }
</style>