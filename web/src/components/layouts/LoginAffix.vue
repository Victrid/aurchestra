<template>
  <el-affix :offset="1">
    <router-link to="/admin">
    <el-button type="primary" 
    style="font-weight: bold;
      font-size:12pt;
      height:3.5em;
      max-height:4em;
    ">Administrator</el-button>
    </router-link>
  </el-affix>
</template>

<script>
export default {
  name: 'LoginAffix',
  data(){
      return{
      }
  },
  computed:{

  },
  methods:{
  },
  props: {
      
  },
}
</script>

<style >
.el-affix--fixed .el-button{
  background: rgba(2, 51, 131, 0.048);
  border-width: 0pt;
}

.el-affix{
  position: absolute;
  right: 3pt;
}
</style>