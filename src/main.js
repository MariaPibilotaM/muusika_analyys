import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import VueFileAgent from 'vue-file-agent';

Vue.use(VueFileAgent);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
