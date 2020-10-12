<template>
    <b-container fluid>
      <b-navbar toggleable="lg" type="dark" variant="dark">
        <b-navbar-brand href="#">NIRS</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
          <b-nav-item v-for="item in headData.headers" :key="item.id" href="item.url">{{item.text}}</b-nav-item>
            <!-- <b-nav-item href="#">首页</b-nav-item>
            <b-nav-item href="#">数据分析</b-nav-item>
            <b-nav-item href="#">产品购买</b-nav-item>
            <b-nav-item href="#">学习专区</b-nav-item>
            <b-nav-item href="#">联系我们</b-nav-item> -->
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-form>
              <b-form-input size="sm" class="mr-sm-2" placeholder="请输入搜索内容"></b-form-input>
              <b-button size="sm" class="my-2 my-sm-0" type="submit">查询</b-button>
            </b-nav-form>

            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template v-slot:button-content>
                <em>个人中心</em>
              </template>
              <b-dropdown-item href="#">个人信息</b-dropdown-item>
              <b-dropdown-item href="#">退出登录</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </b-container>
</template>

<script>
import { GetCates } from "../apis/read.js";
import { reactive,ref } from "@vue/composition-api";

export default {
  name:"Header",
  setup(props, context){ //setup相当于beforeCreate，props是父组件传入的内容，context是当前组件内容
    const headData= reactive({
      headers:[]
    });
    GetCates().then(reponse => {
      console.log("In header reponse = ", reponse.data.data);
      headData.headers = reponse.data.data;
      console.log("headData.header = ", headData.headers)
    });

    return {
      headData
    }

  }
}
</script>

<style lang = "scss" scoped>

</style>