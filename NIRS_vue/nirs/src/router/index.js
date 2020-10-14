import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import HomeCate from "../views/HomeCate.vue"

Vue.use(VueRouter);

const routes = [
  {//网站首页
    path: "/",
    name: "Home",
    component: Home
  }, 

  //板块分类页面
{
  path:"/:cate_id",
  name:"HomeCate",
  component: HomeCate
}
];




const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
