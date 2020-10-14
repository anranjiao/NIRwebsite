<template>
    <div id = "HomeCate">
        <Header />
        <b-container>
            <b-row>
                <b-col cols = "12" md = "7">

                    <h6>最新订单</h6>
                        <table role="table" aria-busy="false" aria-colcount="3" class="table b-table table-striped table-hover" ><!----><!---->
                            <thead role="rowgroup" class=""><!---->
                            <tr role="row" class="">
                                <th role="columnheader" scope="col" aria-colindex="1" class=""><div>order_id</div></th>
                                <th role="columnheader" scope="col" aria-colindex="2" class=""><div>commmets</div></th>
                                <th role="columnheader" scope="col" aria-colindex="3" class=""><div>order_date</div></th></tr>
                            </thead>
                            <tbody role="rowgroup"><!---->
                                <tr role="row" v-for="item in items.newestItem" :key="item.id">
                                <td aria-colindex="1" role="cell" class="" >{{item.order_id}}</td>
                                <td aria-colindex="2" role="cell" class="">{{item.comments}}</td>
                                <td aria-colindex="3" role="cell" class="">{{dateFormat(item.order_date)}}</td></tr>
                                
                            </tbody><!---->
                        </table>

                </b-col>
                <b-col cols = "12" md = "1">
                    
                </b-col>
                <b-col cols = "12" md = "4">
                    <h6>积分排行榜</h6>
                </b-col>
            </b-row>
        </b-container>
        <Footer />
    </div>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import {ref,reactive,onMounted} from "@vue/composition-api";
import {GetInfoPost} from "../apis/read.js";
import  dateFormat from "../utils/date.js";

export default {
    name:"HomeCate",
    components:{
        Header,
        Footer

    },

    setup(props,context){
        const now_url = ref(context.root.$route.path)
        
        const newstParams = reactive({
            url: now_url.value,
            key:'newest'
        })

        const items = reactive({
            newestItem:[]
        })

        const mostParams = reactive({
            url: now_url.value,
            key:'most'
        })

        GetInfoPost(newstParams).then(resp => {
            console.log("resp.data.data",resp.data.data);
            items.newestItem = resp.data.data
        });

        onMounted(()=>{
            console.log("In HomeCate now_url=", now_url);
            console.log("In HomeCate now_url.value=", now_url.value);
        });

        return {
            items,
            dateFormat
        }
    }
    
}
</script>

<style lang="scss" scoped>

</style>