import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [
        {
            path: "/",
            alias: "/messages",
            name: "messages",
            component: () => import("./components/MessagesList")
        },
        {
            path: "/add",
            name: "add",
            component: () => import("./components/AddMessage")
        }
    ]
});
