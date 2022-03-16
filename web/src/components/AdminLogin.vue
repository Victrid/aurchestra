<template>
    <div class="admin">
        <el-card>
            <h2>Login</h2>
            <el-form label-position="left" label-width="50px" size="large" ref="formLogin"
            class="login-form">
                <!-- :model="formLogin"
                :rules="rules"-->
                <el-form-item  prop="name" class="admin-item">
                    <el-input placeholder="Username"
                    v-model="username"
                    ></el-input>
                </el-form-item>
                <el-form-item  prop="password" class="admin-item">
                    <el-input placeholder="Password"
                    type="password"
                    v-model="password"
                     ></el-input>
                </el-form-item>
                <el-form-item>
                    <el-button
                        class="login-button"
                        type="primary"
                        native-type="submit"
                        block
                        @click="login"
                    >
                    Login</el-button>
                </el-form-item>
            </el-form>
        </el-card>

        <div class="footer" style="margin-top:auto">
            <hr />
            <div class="version" style="color:black">Version 0.01</div>
        </div>
    </div>
</template>

<script >

export default{
    name: "AdminLogin",
    data(){
        return{
            username:"",
            password:""
        }
    },
    methods:{
        login(){
            console.log(Date())
        }
    }
}
</script>


<style>
.admin {
    flex: 1;
    display: flex;
    justify-content: center;
    align-items: center;
}
.login-button {
  width: 100%;
  margin-top: 40px;
}
.login-form {
  width: 290px;
}
.footer{
    padding: 20px 20px;
  color: #f0f4f8;
  display: flex;
  flex-direction: column;
  align-items: center;
}


</style>
<style >
$teal: rgb(0, 124, 137);
.admin .el-button--primary {
  background: $teal;
  border-color: $teal;

  &:hover,
  &.active,
  &:focus {
    background: lighten($teal, 7);
    border-color: lighten($teal, 7);
  }
}
.admin .el-input__inner:hover {
  border-color: $teal;
}
.admin .el-input__prefix {
  background: rgb(238, 237, 234);
  left: 0;
  height: calc(100% - 2px);
  left: 1px;
  top: 1px;
  border-radius: 3px;
  .el-input__icon {
    width: 30px;
  }
}
.admin .el-input input {
  padding-left: 35px;
}
.admin .el-card {
  padding-top: 0;
  padding-bottom: 30px;
}
.admin .el-card {
    width: 340px;
    display: flex;
    justify-content: center;
}
</style>