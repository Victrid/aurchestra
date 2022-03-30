<template>
  <div class="intro-card frame px-3 py-4 testdb">
    <div class="row level">
      <div class="col-xs-3 level-item">
        <p class="m-0">Name:</p>
      </div>
      <div class="col-xs-9 level-item">
        <input type="name" v-model="itemName" />
      </div>
    </div>
     <!-- Url -->
     <div class="row level">
      <div class="col-xs-3 level-item">
        <p class="m-0">Addr:</p>
      </div>
      <div class="col-xs-9 level-item">
        <input type="url" v-model="itemAddr" />
      </div>
    </div>
    <!-- Email -->
    <div class="row level">
      <div class="col-xs-3 level-item">
        <p class="m-0">Email:</p>
      </div>
      <div class="col-xs-9 level-item">
        <input type="email" v-model="itemEmail" />
      </div>
    </div>
   
   
    <button type="submit" class="btn-xs text-blue-600 pull-right" @click=additem>提交</button>
  </div>
  
</template>

<script>
export default {
  name: "testDB",
  data(){
      return{
          itemName:"Test1",
          itemAddr:"www.baidu.com",
          itemEmail:"yfqing@sjtu.edu.cn"
      }
  },
  methods:{
      additem(){
          console.log("点击我")
          console.log(this.itemName)
        
      }
  }
};
</script>


<style>
.intro-card {
  background-color: rgba(255, 255, 255, 0.5);
  max-width: 60%;
  min-width: 350px;
  position: absolute;
  left:40%;
}
</style>
