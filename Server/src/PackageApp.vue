
<script >
export default {
  name: "PackageApp",
  data() {
    return {
      title1: "Name",
      title2: "Address",
      title3: "State",
      packName:"Please input the package Name......",
      packAddr:"Please input the git address......",
      conEmail:"",
      is_open:false,
      result:"",
    };
  },
  mounted() {

  },
  computed: {
    
  },
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
          (v) => this.result = (v.status==201)?'Apply Success!':'')
          .then(this.show_result=true).then(
          setTimeout(()=>{
            if (this.result=='Apply Success!'){
              window.location.href = 'http://'+baseURL
            }else{
              alert('The package has been already in the system.')
            }
          },1000)
        )
      }

  },
};
</script>

<style>
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
  color: rgb(0, 229, 255);
  font-style: italic;
}
.table td.state {
  font-size: 1.3em;
  color: rgb(37, 255, 109);

}

.table {
  width: 80%;
}
.add-btn{
  position:fixed;
  left:90%;
  width: 8%;
  font-size:1em;
  color: rgb(66, 195, 255);
  font-weight: bolder;
  background: rgba(45, 60, 7, 0.275);
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