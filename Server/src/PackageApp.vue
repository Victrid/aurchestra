<template lang='pug'>
button.outline.u-shadow-xl.add-btn(@click="open") Request

table.table.striped
  thead
      tr
          th 
              abbr(title="Title1") {{ title1 }}
          th 
              abbr(title="Title2") {{ title2 }}
          th 
              abbr(title="Title3") {{ title3 }}
          th
              abbr(title="Title4") {{ title4 }}
  tbody     
      tr(v-for="item in data")
          td.name {{item.name}}
          td.link 
              a(v-bind:href="item.addr")  {{item.addr}}               
          td(v-bind:class="getState(item.state)") {{item.state}}
          td.time 2 hours ago
#help
  h1.headline-6(style="color:white" align='center') Manaual
  .desp
      p Here is a manual to help you understand and use 
        span.sign Aurchestra.
  .sub-desp
    .card.question-card1
        div(class="card__header")
            p.font-bold How to submit a new package request?
        .content
            p If a package needed can not be found in the corresponding OS page, 
                span you can click the&nbsp
                span.apply-btn  APPLY 
                span &nbsp button in the uppre right corner to submit a new package compilation request.
            p Once checked by admin, it will be added into page together with its current state.
            p However, it is not available for installing until the compilation is complete, 
                span which can be comfirmed if the state shows "
                span(style="color:green;font-weight:bold") Available
                span ".
    .card.question-card2
        div(class="card__header")
            p.font-bold How to configure in Arch Operating System?
        .content
            p.tbd TBD...
//- 
div.card.animated.bounceIn(v-if="is_open" @close="close()")
  div.card__header
      p.title Apply to add a new package to Aurchestra :
  div.content
      //- package Name
      .row.level
      .col-xs-3.level-item
          p.m-0.text-info.font-bold.text-lg Package Name*:
      .col-xs-9.level-item
          input(type="name"  v-model="packName" placeholder="Please input the package Name......")
      //- Git Address
      .row.level
      .col-xs-3.level-item
          p.m-0.text-info.font-bold.text-lg Package Address*:
      .col-xs-9.level-item
          input(type="url"  v-model="packAddr" placeholder="Please input the git address......")
      //-  Email
      .row.level
      .col-xs-3.level-item
          p.m-0.text-info.font-bold.text-lg Connect Email:
      .col-xs-9.level-item
          input(type="email" v-model="conEmail" placeholder="optional")
      p.text-md (We will use this email to keep you updated on the status of your application submission)
      div.card__action-bar.u-center
          button.btn-transparent.outline.mx-4(@click="cancel") Cancel
          button.btn-transparent.outline.mx-4(@click="submit") Submit
      p.text-ls.results(v-if="show_result" align='center') {{result}}
</template>


<style>

</style>
<script >
export default {
  name: "PackageApp",
  data() {
    return {
      title1: "Name",
      title2: "Address",
      title3: "State",
      title4: "Last Modified",
      data:[],
      packName:"",
      packAddr:"",
      conEmail:"",
      is_open:false,
      result:"",
      baseURL:"",
      requestAPI:"",
      getDataAPI:"",
    };
  },
  mounted() {
    this.baseURL = 'http://'+ window.location.hostname+':'+window.location.port+window.location.pathname;
    this.requestAPI =this.baseURL+'/api/submit'
    this.getDataAPI = this.baseURL+'/api/getList'
    // console.log(this.baseURL)
    //get the list
    this.axios
      .get(this.getDataAPI).catch((error)=>{
        console.warn(error);
      }).then((v) => {
        console.log(v.data)
        this.data=v.data
      })
  },
  computed: {
  },
  components: {
  },
  methods: {
    getState(state){
      if(state=="Waiting to Compile..."){
        return "waitPac"
      }else if(state=="Compiling..."){
        return "compPac"
      }else{
        //Available
        return "availPac"
      }
    },
    open(){
      console.log("增加新的条目!")
      if (this.is_open==false){
        this.is_open=true
      }
    },
    cancel(){
      console.log("取消申请!")
      this.is_open=false
    },
    submit(){
      console.log(`提交申请:
      Name: ${this.packName}\n 
      Addr: ${this.packAddr} \n
      Email: ${this.conEmail}
      `)
      let tmp = this.conEmail
      if (tmp === ""){
        tmp = null
      }
      let item = {
      "name": this.packName,
      "addr": this.packAddr,
      "email": tmp,
      "state": 0
      }

      // console.log(api);
      this.axios.post(this.requestAPI, item).catch((error) => {
        console.warn(error);}).then(
          (v) => this.result = (v.status==201)?'Apply Success!':'')
          .then(this.show_result=true).then(
          setTimeout(()=>{
            if (this.result=='Apply Success!'){
              window.location.href = this.baseURL
            }else{
              alert('The requested package exists in the repository.')
            }
          },1000)
        )
      }

  },
};
</script>

<style scoped>
/* Titile attributes */
.table abbr {  
  font-size: 20pt;
  color: rgba(199, 199, 199, 0.905);
  align-self: flex-start;
}

.table td.name {
  font-size: 1.5em;
  color: rgba(255, 254, 254, 0.928);
  font-weight: bolder;
}

.table td.link a{
  font-size: 1.3em;
  color: #b1b1f1;
  font-weight:normal;
  /* font-style: italic; */
}
.table td.waitPac {
  font-size: 1.3em;
  color: rgb(255, 102, 37);
  font-weight: bold;
}
.table td.compPac {
  font-size: 1.3em;
  color: rgb(244, 255, 37);
  font-weight: bold;
}
.table td.availPac {
  font-size: 1.3em;
  color: rgb(70, 255, 37);
  font-weight: bold;
}
.table td.time {
  font-size: 1.3em;
  color: rgb(237, 239, 237);
  font-weight: thin;
}
.table {
  width: 50%;
  margin-left: 5%;
}
.add-btn{
  position:fixed;
  right: 9%;
  top:0%;
  z-index: 1000;
  width: 6%;
  font-size:1em;
  color: rgb(6, 10, 12);
  font-weight: bolder;
  background: rgba(45, 60, 7, 0.275);
  text-transform: unset !important;
}
#packagelist .card{
  max-width: 60%;
  position: absolute;
  left:35%;
  top:20%;
  padding: 1%;
  opacity: 0.95;
}
.card .title{
  font-size: 25px;
}
.card .content{
  font-size: 30px;
}
.card .card__action-bar button{
  font-size: 25px;
}
.card.input{
  font-size:20px
}
/* manaual css */
#help{
  position:fixed;
  right:1%;
  /* margin-left: 2%; */
  max-width: 40;
  top:8%
}
#help .desp p{
    /* margin-right: 1%; */
    color:white;
    font-size: 1.5em;
    line-height:normal;
}
#help .sub-desp{
  position: fixed;
  right: 2%;
  width: 1000px;
}
#help .sign{
    color: rgb(73, 222, 255);
    font-weight: bolder;
}
#help .card__header p{
    font-size:1.4em;
    color: rgb(199, 0, 0);
    font-weight: bold;
}
#help .sub-desp .question-card1{
  margin-top: 3%;
  width:550px;
  min-width: 550px;
}
#help .sub-desp .question-card1{
  margin-top: 25%;
  width:550px;
  min-width: 550px;
}
#help .card .content p{
    font-size: 0.8em;
    line-height: 1.2em;
}
#help .apply-btn{
    color:rgb(192, 112, 0);
    font-weight: bold;
    background: rgba(175, 175, 175, 0.812);
    border-radius: 5px;
}
#help .tbd{
    color:red;
}



</style>