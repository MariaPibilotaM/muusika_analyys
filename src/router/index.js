import Vue from "vue";
import VueRouter from "vue-router";
import LandingPage from "../components/landing/LandingPage";
import AnalysisPage from "../components/analysis/AnalysisPage";
import Reference from "../components/Reference";
import MusicDescription from "../components/analysis/MusicDescription";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "AVALEHT",
        component: LandingPage
    },
    {
        path: "/kirjelda",
        name: "Analüüs",
        component: AnalysisPage
    },
    {
        path: "/kirjelda/tulemus",
        name: "Tulemus",
        component: MusicDescription
    },
    {
        path: "/allikad",
        name: "Allikad",
        component: Reference
    }

];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes
});

export default router;
