<template >
  <!-- <img alt="ProjectLogo" class="HomeLogo" :src="archLogo"  /> -->
  <img alt="archlogo" id="home-logo" src="../assets/arch.png" class="el-image__inner">
  
  <p id="introduction">
    Aurchestra is an automated package build orchestration system.
  </p>
  <p id="details">
    Designed to establish a distributed, reproducible, and easy-to-manage
    software package build process.
  </p>
</template>

<script>
export default {
  data() {
    return {

    };
  },
  props: {},
};
</script>

<style >
#home-logo{
  margin-top: 3em;
  height:14em;
  width:12em;
  align-self: center;
}

#introduction{
    font-size: 20pt;
    color: rgb(250, 250, 250);
}
#details{
  font-size: 16pt;
  color:rgba(228, 224, 224, 0.726);
}
</style>