<template>
    <div>
        <div class="header-container">
            <img class="header-blob" src="../../assets/svgs/blob_green.svg">
            <div class="main-header-font-gray header">Analüüs</div>
        </div>
        <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column" v-if="info.nimi !== undefined">
            <div class="description-header">
                <h4>{{info.nimi}}</h4>
            </div>
            <div class="tempo description">
                <h4><i class="bi bi-speedometer2"></i> {{info['bpm']}} bpm </h4>
                <p class="lead-gray lead">{{this.tempoTutvustus}}</p>
                <div class="scale">
                    Energilisus
                    <div class="progress">
                        <div class="progress-bar energy" role="progressbar" :style="{width:energia + '%'}"
                             aria-valuemin="0"
                             aria-valuemax="100">{{energia}}%
                        </div>
                    </div>
                </div>
                <div class="scale">
                    Tantsitavus
                    <div class="progress">
                        <div class="progress-bar dance" role="progressbar" :style="{width:tantsitavus + '%'}"
                             aria-valuemin="0" aria-valuemax="100">{{tantsitavus}}%
                        </div>
                    </div>
                </div>
            </div>
            <div class="key description">
                <h4><i class="bi bi-music-note-beamed"></i> {{pitch}} </h4>
                <p class="lead-gray lead">{{helistik}}</p>
                <img :src="link" style="width: 20%">
            </div>
            <div class="tags description">
                <h4><i class="bi bi-chevron-double-right"></i><i class="bi bi-chevron-double-right"></i> Tempo
                </h4>
                <p class="lead-gray lead">{{this.data['saate-lause'][nr(0,2)]}}</p>
                <p class="lead-gray lead tempos" v-for="(item, index) in tempoMuutus" :key="index">
                    - {{item}}
                </p>
            </div>
            <div class="key description">
                <h4><i class="bi bi-rainbow"></i> Kulminatsioon </h4>
                <p class="lead-gray lead">{{kulminatsioon}}</p>
            </div>
            <div class="tags description">
                <h4 class="right-header"><i class="bi bi-tags"></i> Märksõnad </h4>
                <p class="lead-gray lead">Pala saab iseloomustada järgnevate märksõnadega:
                    {{data.tagg[info.taggs[0]].nimi+', '+ data.tagg[info.taggs[1]].nimi+', '+
                    data.tagg[info.taggs[2]].nimi+' ning '+ data.tagg[info.taggs[3]].nimi}} .</p>
                <p class="lead-gray lead tagg-desc" v-if="data.tagg[info.taggs[0]].vaste !== ''">
                    {{data.tagg[info.taggs[0]].vaste}}
                </p>
                <p class="lead-gray lead tagg-desc" v-if="data.tagg[info.taggs[1]].vaste !== ''">
                    {{data.tagg[info.taggs[1]].vaste}}
                </p>
                <p class="lead-gray lead tagg-desc" v-if="data.tagg[info.taggs[2]].vaste !== ''">
                    {{data.tagg[info.taggs[2]].vaste}}
                </p>
                <p class="lead-gray lead tagg-desc" v-if="data.tagg[info.taggs[3]].vaste !== ''">
                    {{data.tagg[info.taggs[3]].vaste}}
                </p>
            </div>
        </div>
    </div>
</template>

<script>
    import descriptionData from '../../data/descriptionData'
    import axios from "axios";

    export default {
        name: "MusicDescription",
        data() {
            return {
                tempoTutvustus: '',
                data: descriptionData,
                energia: '',
                tantsitavus: '',
                kulminatsioon: '',
                tempoMuutus: [],
                culmination: {},
                helistik: '',
                pitch: '',
                duur: descriptionData.duur,
                moll: descriptionData.moll,
                link: '',
                info: {},
                italian: '',
            }
        },
        methods: {
            italianTerm(val) {
                let t = this.data.tempod;
                for (let i = 0; i < t.length; i++) {
                    if (t[i][0] <= val && val <= t[i][1]) {
                        return this.data.termin[i];
                    }
                }
            },
            nr(min, max) {
                return Math.floor(Math.random() * (max - min) + min) + '';
            },
            tempChange(letter, val, temp) {
                if (val > temp + 10) {
                    let term = this.italianTerm(val);
                    if (term !== this.italian) {
                        this.tempoMuutus.push(this.data.kiirem[this.nr(0, 4)].replaceAll('[nr]', letter).replaceAll('[tempo]', val).replaceAll('[term]', term));
                    } else
                        this.tempoMuutus.push(this.data['sama-kiirem'][this.nr(0, 3)].replaceAll('[nr]', letter).replaceAll('[tempo]', val).replaceAll('[term]', term));

                } else if (temp - 10 > val) {
                    let term = this.italianTerm(val);
                    if (term !== this.italian) {
                        this.tempoMuutus.push(this.data.aeglasem[this.nr(0, 4)].replaceAll('[nr]', letter).replaceAll('[tempo]', val).replaceAll('[term]', term));
                    } else
                        this.tempoMuutus.push(this.data['sama-aeglasem'][this.nr(0, 3)].replaceAll('[nr]', letter).replaceAll('[tempo]', val).replaceAll('[term]', term));
                }
            },
            loadData() {
                const path = 'http://prog.keeleressursid.ee/veebid/muusika_analyys/data';
                axios.get(path)
                    .then((res) => {
                        this.info = res.data.data;
                        if (this.info.nimi !== undefined) {
                            this.energia = Math.round(this.info['energia']);
                            this.tantsitavus = Math.round(this.info['tantsulisus']);
                            this.italian = this.italianTerm(this.info.bpm);
                            this.culmination = this.info.kulminatsioon;
                            this.fillGaps();
                        }
                    })
                    .catch((error) => {
                        console.error(error);
                    });
            },
            fillGaps() {
                // Filling gaps in key description
                let isMajor = this.info.helistik['helilaad'] !== 'minoor';
                let indx = isMajor ? this.duur.indexOf(this.info.helistik.nimi) : this.moll.indexOf(this.info.helistik.nimi);
                let metadata = this.data.helistikud[indx];

                this.pitch = (isMajor ? metadata.duur : metadata.moll);
                let number = metadata.märk;
                let desc = number === '' ? this.data['ilma-märgita'] : this.data['märgiga'];
                this.link = metadata['link'];
                let v6ti = metadata['võtmemärk'];
                let m2rk1 = '';
                let m2rk2 = '';
                for (let i = 0; i < number; i++) {
                    let m = this.data[v6ti][i];
                    let n = this.data[v6ti + '2'][i];
                    m2rk1 += ' ' + m;
                    m2rk2 += ' ' + n;
                    if (i + 1 !== number) {
                        m2rk1 += ', ';
                        m2rk2 += ',';
                    }
                }
                let valik = this.nr(0, 3);
                let laused = (isMajor ? this.data.mažoor[valik] : this.data.minoor[valik]);
                this.helistik = desc[valik].replaceAll('[noot]', this.pitch)
                    .replaceAll('[nr]', number).replace('[märk]', m2rk1)
                    .replaceAll('[vastas]', isMajor ? metadata.moll : metadata.duur)
                    .replaceAll('[võtmemärk]', v6ti)
                    .replaceAll('[märk2]', m2rk2)
                    .replaceAll('[0]', laused[0])
                    .replaceAll('[1]',laused[1])
                    .replaceAll('[2]',laused[2]);

                // Filling gaps in tempo description
                let lause = this.data.bpm[this.nr(4, 9)].replace('[termin]', this.italian).replace('[om]', this.data[this.italian].omadus).replace('[vahemik]', this.data[this.italian].vahemik);
                this.tempoTutvustus = this.data.bpm[this.nr(0, 3)].replace('[tempo]', this.info.bpm) + lause.charAt(0).toUpperCase() + lause.substring(1);

                // Filling gaps in culmination description
                let aeg = this.culmination['m'] + ':' + (this.culmination['s'] < 10 ? '0' : '') + this.culmination['s'];
                this.kulminatsioon = this.data.kulminatsioon[this.nr(0, 3)].replace('[min]', aeg);

                let temp = this.info.bpm;
                if (temp - 10 <= Math.round(this.info.a) && Math.round(this.info.a) <= temp + 10 &&
                    temp - 10 <= Math.round(this.info.b) && Math.round(this.info.b) <= temp + 10 &&
                    temp - 10 <= Math.round(this.info.c) && Math.round(this.info.c) <= temp + 10) {
                    this.tempoMuutus.push(this.data["pole-muutus"][this.nr(0, 2)]);
                } else {
                    this.tempChange("I", Math.round(this.info.a), temp);
                    this.tempChange("II", Math.round(this.info.b), temp);
                    this.tempChange("III", Math.round(this.info.c), temp);
                }
            }
        },
        mounted() {
            this.loadData();
        }
    }
</script>

<style scoped>
    .description {
        padding-bottom: 3rem;
    }

    .key {
        width: 70%;
        margin-right: 0;
        text-align: right;
    }

    .tags {
        width: 70%;
        margin-left: 0;
    }

    .progress-bar {
        background-color: #20bdb2;
    }

    .scale {
        padding-bottom: 1rem;
        width: 90%;
    }

    .description-header {
        display: flex;
        justify-content: center;
        flex-flow: row nowrap;
        align-items: flex-end;
        gap: 2rem;
    }

    .tempo {
        margin-top: 3rem;
        width: 70%;
        margin-left: 0;
    }

    .tempos {
        padding-top: 0px;
    }

    .tagg-desc {
        padding-top: 0px;
    }

</style>