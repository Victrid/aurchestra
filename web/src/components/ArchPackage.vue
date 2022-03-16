<template>
    <br />
    <br />
    <div>
    <el-input class="el-input" v-model="value"></el-input>
    <el-button @click="search">search</el-button>
    </div>
    <el-descriptions  column=1 class="packages" >
        <el-descriptions-item class="package-item" >
            <el-row>
                <p class="package-name">Package name</p>
                <p class="package-state">Compling...</p>
            </el-row>
        </el-descriptions-item>
        <el-descriptions-item class="package-item">
        <el-row>
                <p class="package-name">Package name2</p>
                <p class="package-state">Compling...</p>
            </el-row>
        </el-descriptions-item>

    </el-descriptions>
    <!-- <p>This is Arch</p> -->
</template>

<script >
export default{
    mounted(){
        console.log("访问后端服务器以得到列表")
    },
    name: "ArchPackage",
    data(){
        return{
            value:""
        }
    },
    methods:{
        search(){
            console.log(Date())
        }
    }
}
</script>


<style>
.el-input{
    width:20%;
    margin:10pt;
}
.package-state{
    position: absolute;
    right:5em
}
.package-name{
    font: size 8pt;
    color: white;
}
.package-item{
    margin:5pt;
}
.packages{
    margin-left: 5%;
    margin-right: 2%;
   
}

.el-descriptions__body .el-descriptions__table  .el-descriptions__cell {
    background: rgba(209, 208, 208, 0.041);
     margin:5pt;
    
}
.el-descriptions__body{
    background: rgba(6, 15, 65, 0);
}
</style>