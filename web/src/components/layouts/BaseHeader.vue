<template>
    <el-menu id="menu" mode="horizontal" 
    text-color="#ffffff"  background-color="#212122ad" 
    default-active="2" router
    >
        <el-menu-item index="/" class="header-item" router
            @click="this.OSmsg=`Supported OS`"
        >
            <el-image alt="homeloge" id="header-logo" :src="HeaderLogo"></el-image>
        </el-menu-item>
        <el-sub-menu class="header-item" text-color="#00000">
            <template #title >{{OSmsg}}</template>
            <el-menu-item  index="arch" class="header-item" style="size:20pt" 
            router @click="this.OSmsg=`Arch`;"
            >Arch Linux</el-menu-item>
            <el-menu-item  class="header-item"  disabled>TBD...</el-menu-item>
        </el-sub-menu>
    </el-menu>

</template>

<script>
const HeaderLogo = require('../../assets/arch.png')
export default {
  name: 'BaseHeader',
  data(){
      return{
          HeaderLogo,
          OSmsg:"Supported OS"
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
    
<style>
#menu{
  background: #2c3e50;
}
.header-item{
    max-height: 4em;
    align-self: center;
}
.header-item #header-logo{
    width : auto;
    max-height: 4em;
    align-self: center;
    align-content: center;
    align-items: center;
}
.el-sub-menu .el-sub-menu__title{
    font-size: 14pt;
    font-style:oblique;
}
</style>