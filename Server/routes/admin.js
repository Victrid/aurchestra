var express = require('express');
var router = express.Router();
const { models } = require('../sequelize');
var bcrypt = require('bcrypt')
const axios=require('axios')

const watcherAPI = process.env.DAEMON_CONNECTION ?
process.env.DAEMON_CONNECTION : require('../config/daemon.connect.config');


// const { Op } = require("sequelize");

router.get('/', function(req, res, next) {
    res.render('admin', { title: 'Admin'});
  });


async function check_valid(req,res) {

  // console.log('===============')
  var name = req.body.username
  var password = req.body.password

  // console.log("Name:", name)
  const user = await models.admin.findAll({
    where: {
      username: name
    }
  });

  if (user.length==0){
    res.status(200).send('fail')
    return false;
  }
  
  var str=JSON.stringify(user.at(0),null,2);
  const json = JSON.parse(str)
  // console.log("Result:", json.password);
  if ((await bcrypt.compare(password, json.password)).valueOf()){
    // console.log("check success")
    res.status(201).send('success')
    // req.session.userName = name
    // console.log("SESSION Changed:",req.session.userName)
    return true
  }else{
    console.log("check fail")
    res.status(200).send('fail')
    return false
  }
};


router.post('/api/login',function(req,res,next){
  check_valid(req,res).then((v)=>{
    console.log("Validation:",v)
  })
});


async function get_package(req,res) {
  const checked = await models.softwareinfo.findAll({
    where: {
      state: 0
    }
  });
  var checkedStr=JSON.stringify(checked,null,2);
  const checkedJson = JSON.parse(checkedStr)
  //- 1: 等待编译 - 2: 编译完成
  //- 6: 编译错误 - 7: 等待删除
  // 1 2 
  var states = [1,2]
  var existedJson = [];
  for (const i in states){
    // console.log(states[i])
    const tmped = await models.softwareinfo.findAll({
      where: {
       state: states[i]
      }
    });
    var tmpStr=JSON.stringify(tmped,null,2);
    const tmpJson = JSON.parse(tmpStr)
    // for (var item in tmpJson) {
    //   console.log("条目",tmpJson[item])
    //   // console.log("key",tmpJson[item])
    // }
    existedJson.push(...tmpJson)
  }
  //6
  const wrong = await models.softwareinfo.findAll({
    where: {
      state: 6
    }
  });
  var wrongStr=JSON.stringify(wrong,null,2);
  const wrongJson = JSON.parse(wrongStr)
  // console.log(existedJson)
  
  var data={
    toBeCheck: checkedJson,
    Checked: existedJson,
    wrongList: wrongJson,
  }
  res.send(data)
}

router.get('/api/getList',function(req,res,next){
  get_package(req,res).then((v)=>{
    
  })
});

async function update_state(req,res,aimState){
  // console.log(req.body)
  // console.log(req.body.packageName)
  await models.softwareinfo.update({state:aimState},{
    where: {
     name: req.body.packageName
    }
  });
  res.status(201)
}
async function reject_item(req,res){
  // console.log(req.body)
  // console.log(req.body.packageName)
  await models.softwareinfo.destroy({
    where: {
     name: req.body.packageName
    }
  });
  res.status(201)
}

router.post('/api/pass',function(req,res,next){
  update_state(req,res,1).then((v)=>{
  })
});

router.post('/api/reject',function(req,res,next){
  reject_item(req,res).then((v)=>{
  })
});

router.post('/api/delete',function(req,res,next){
  update_state(req,res,7).then((v)=>{
  })
});
async function watcher(req,res){
  console.log("invoke daemon process...")
  console.log(req.body)
  axios.post(watcherAPI,req.body).catch((error) => {
    console.warn(error);})
}  
router.post('/api/watcher',function(req,res,next){
  watcher(req,res).then((v)=>{
    // console.log(v)
  })
});

async function getLog(req,res){
  var package = req.body.packageName
  const info = await models.loginfo.findAll({
    where: {
      name: package
    }
  });
  if(info.length==0){
    //no logs
    res.send("Logs miss temporarily...")
    return
  }
  var str=JSON.stringify(info.at(0),null,2);
  const json = JSON.parse(str)
  res.send(json.loginfo)
}

router.post('/api/getlog',function(req,res,next){
  console.log("query log: package",req.body)
  getLog(req,res).then((v)=>{
    // console.log(v)
  })
});

module.exports = router;