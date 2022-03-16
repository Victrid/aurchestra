<template>
  <BaseHeader/>
  <hr/>
  <LoginAffix/> 
  <router-view keep-alive></router-view>
</template>

<script>
// import HomePage from './components/HomePage.vue'
import BaseHeader from './components/layouts/BaseHeader.vue'
import LoginAffix from './components/layouts/LoginAffix.vue'
export default {
  name: 'App',
  components: {
    // HelloWorld,
    // HomePage,
    BaseHeader,
    LoginAffix,
  } 
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
body {
  margin: 0;
  padding: 0;
  background: #102a43;
  background-size: contain;
}

</style>
