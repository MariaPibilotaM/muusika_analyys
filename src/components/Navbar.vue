<template>
    <div class="menu">
        <div class="navigation-icon">
            <nav class="navbar navbar-light bg-dark">
                <div class="container-fluid">
                    <div v-if="showNav">
                        <div class="navigation" @click="nav">
                            <router-link to="/">AVALEHT</router-link>
                            <router-link to="/kirjelda">ANALÜÜS</router-link>
                            <router-link to="/allikad">ALLIKAD</router-link>
                        </div>
                    </div>
                    <button class="navbar-toggler" type="button" @click="nav">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                </div>
            </nav>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Navbar",
        data() {
            return {
                showNav: false
            }
        },
        methods: {
            nav() {
                this.showNav = !this.showNav;
            }
        }
    }
</script>

<style scoped>
    .navigation {
        display: flex;
        flex-flow: row nowrap;
        gap: 3rem;
        align-items: flex-end;
        padding-right: 3rem;
    }

    a {
        color: black;
    }

    .bg-dark {
        background-color: transparent !important;
    }

    .menu {
        position: absolute;
        right: 3rem;
        top: 2rem;
    }
a:hover{
    color: black;
    text-decoration:none
}

</style>