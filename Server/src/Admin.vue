<template lang='pug'>
.div(v-if="loggedIn")
  h2(style="color: white") Welecom: {{ admin }}
  h3(style="color: white") Packages to be reviewed:
  table.table.striped(align="center")
    thead
      tr
        th 
          abbr(title="Title1") {{ title1 }}
        th 
          abbr(title="Title2") {{ title2 }}
        th 
          abbr(title="Title3") {{ title3 }}
        th
          abbr(title="Title3") {{ title4 }}
    tbody 
      tr(v-for="item in toBeCheckedList")
        td {{ item.name }}
        td {{ item.addr }}
        td {{ item.email }}
        td 
          button.mr-2(@click="pass_item(item)") pass
          button.ml2(@click="reject_item(item)") reject

  h3(style="color: white") Manage existing packages:
  table.table.striped(align="center" )
    thead
      tr
        th 
          abbr(title="Title1") {{ title1 }}
        th 
          abbr(title="Title2") {{ title2 }}
        th 
          abbr(title="Title3") {{ title2_3 }}
        th
          abbr(title="Title3") {{ title2_4 }}

    tbody 
      tr(v-for="item in existedList")
        td {{ item.name }}
        td {{ item.addr }}
        td {{ item.state }}
        td 
          //- button.mr-2(@click="update_item(item)") update
          button.ml2(@click="delete_item(item)" :disabled="item.state==2") delete
.card.admin-card(style="max-width: 350px", v-else)
  .content.u-text-center.pt-3
    i.fas.fa-user-cog
    .row.level
    .col-xs-3.level-item
      p.m-0.text-info.font-bold.text-lg Admin Account:
    .col-xs-9.level-item
      input(type="name", v-model="admin")
    .row.level
    .col-xs-3.level-item
      p.m-0.text-info.font-bold.text-lg Password:
    .col-xs-9.level-item
      input(type="password", v-model="password")
    br
    button.outline.btn-black(v-on:click="loginFun") login
</template>

<script>
const config = require('../config/guardian.config');
export default {
  name: "Admin",
  data() {
    return {
      title1: "Package",
      title2: "Address",
      title3: "Contact email",
      title4: "Pass",
      title2_3: "State",
      title2_4: "Modify",
      admin: "",
      password: "",
      loggedIn: false, //set true to debug [TODO: set false after debug]
      toBeCheckedList: [],
      existedList: [],
      baseURL: "",
      debug: true,
    };
  },
  computed: {
    listAPI: function () {
      return this.baseURL + "/api/getList";
    },
    loginAPI:function(){
      return this.baseURL + "/api/login";
    },
    passAPI:function(){
      return this.baseURL + "/api/pass";
    },
    rejectAPI:function(){
      return this.baseURL + "/api/reject";
    },
    deleteAPI:function(){
      return this.baseURL + "/api/delete";
    }
  },
  mounted: function () {
    console.log("加载页面...");
    this.baseURL =
      "http://" +
      window.location.hostname +
      ":" +
      window.location.port +
      window.location.pathname;
      if(this.loggedIn){
          this.update_list()
      }
  },
  components: {},
  methods: {
    async update_list() {
      console.log("更新列表...");
      this.axios
        .get(this.listAPI)
        .catch((error) => {
          console.warn(error);
        })
        .then((v) => {
          console.log(v.data);
          this.toBeCheckedList = v.data.toBeCheck;
          this.existedList = v.data.Checked;
        });
    },
    async watcher(item,aimState){
      console.log("通知守护进程...")
      let api = config.ip+":"+config.port;
      let data = {
        name : item.name,
        address: item.addr,
        state: aimState==2? config.addInfo:config.deleteInfo,
      }
      // console.log("api",api)
      // console.log('data',data)
      this.axios.post(api,data).catch((error) => {
          console.warn(error);})
    },
    loginFun() {
      //check input format
      if (this.admin == "") {
        alert("Please input admin account......");
        return;
      }
      if (this.password == "") {
        alert("Please input admin password......");
        return;
      }
      this.axios.post(this.loginAPI, {
        username: this.admin,
        password: this.password,
      }).catch((error) => {
          console.warn(error);
        })
        .then((v) => {
          this.loggedIn = v.status == 201 ? true : false;
          if (!this.loggedIn) {
            alert("The user name or password is incorrect...");
            return;
          }
        })
        .then(() => {
          this.update_list();
        });
    },
    pass_item(item) {
      console.log("申请通过...", item.name);
      // 将item.name传到后端，尤其向数据库请求更改状态->2
      this.axios.post(this.passAPI,{packageName:item.name}).catch((error) => 
      {console.warn(error);}).then(
        this.update_list(),
      ).then(
        //HTTP通知守护进程
        (!this.debug)&& (this.watcher(item,2))
      )
      // 
    },
    reject_item(item) {
      console.log("申请拒绝...", item.name);
      this.axios.post(this.rejectAPI,{packageName:item.name}).catch((error) => 
      {console.warn(error);}).then(
        this.update_list()
      )
    },
    delete_item(item) {
      console.log("删除条目...", item.name);
      
      if(item.state==1||item.state==6){
        // for item state=1,6
        // just delete the item is enough==reject
        this.reject_item(item)
      }else if(item.state==3){
        // for item state==3
        // set state=7 and inform the guardian
         this.axios.post(this.deleteAPI,{packageName:item.name}).catch((error) => 
        {console.warn(error);}).then(
          this.update_list(),
        ).then(
          //inform the guardian
          this.watcher(item,7)
        )
      }else{
        //item state ==0,2,7
        error("should not be here")
      }
     
    },
    update_item(item) {
      console.log("更新条目...", item.name);
      //update name => update name in db and inform 
      
      //update git addr => delete current item and insert a new one

    },
  },
};
</script>

<style>
.admin-card {
  position: absolute;
  left: 40%;
  width: 20%;
}
#admin td{
  color: aliceblue;
}
</style>