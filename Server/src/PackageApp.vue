
<script >
export default {
  name: "PackageApp",
  data() {
    return {
      title1: "Package Name",
      title2: "Addr Link",
      title3: "State",
      packName:"package1",
      packAddr:"http://test.com",
      conEmail:"",
      is_open:false,
      show_result:false,
      result:"",
    };
  },
  mounted() {

  },
  computed: {},
  components: {
  },
  methods: {
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
      let baseURL = window.location.hostname+':'+window.location.port+window.location.pathname;

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
      let api = 'http://'+baseURL+'/api/submit'
      // console.log(api);
      this.axios.post(api, item).catch((error) => {
        console.warn(error);}).then(
          (v) => this.result = (v.status==201)?'Apply Success!':'Apply Fail! Please input right info')
          .then(
        this.show_result=true).then(
          setTimeout(()=>{
            if (this.result=='Apply Success!'){
              window.location.href = 'http://'+baseURL
            }            
          },1000)
        )
    }

  },
};
</script>

<style>
.table abbr {
  font-size: 20pt;
  color: rgb(253, 254, 255);
  align-self: flex-start;
}
.table td {
  align-self: center;
  align-content: center;
}
.table td.name {
  font-size: 22pt;
  color: rgb(26, 59, 250);
  font-style: italic;
  font-weight: bolder;
}
.table td.link {
  font-size: 16pt;
  color: rgb(209, 215, 252);
  font-weight: bold;
}
.table td.state {
  font-size: 16pt;
  color: rgb(228, 230, 241);
  font-style: italic;
  font-weight: bolder;
}
.table td.success {
  font-size: 15pt;
  color: rgb(63, 236, 48);
  font-weight: bolder;
}

.table {
  width: 80%;
}
.add-btn{
  position: absolute;
  right: 4%;
  font-size: 25px;
  color: rgb(228, 243, 90);
  font-weight: bolder;
  background: rgba(23, 82, 146, 0.507);
}
.card{
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
</style>