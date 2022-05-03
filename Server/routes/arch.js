var express = require('express');
var router = express.Router();
const { Op } = require("sequelize");

const { models } = require('../sequelize');


async function getAvailable(req, res) {
  //Displays all feasible packages in alphabetical order
  //including:
  //1 - wait to compile
  //2 - compiling
  //3 - compiled
	const packages = await models.package.findAll({
    where:{
      [Op.or]:[
        {state: 1},
        {state: 2},
        {state: 3}
      ]
    }
  });
  // console.log(packages)
  return packages
};


async function create(req, res) {
  let item = req.body
  // item.push({
  //   'state':0
  // })
  
  //check if the item exists
  
  // console.log(item.name)
  item.name=item.name.trim()
  console.log(item.name)
  const test= await models.package.findAll({
      where:{
        name:item.name,
      }
    }
  )
  if(test.length==0){
    //no such package
    await models.package.create(item);
    res.status(201).send('success')
    return
  }

  var str=JSON.stringify(test.at(0),null,2);
  const json = JSON.parse(str)
  // console.log("==============")
  // console.log(json)
  if(json.state==1&&json.addr==item.addr){
    //wait to check
    res.status(201).send('success')
    return
  }
  console.log("should not be here...")
  res.status(200).send('fail')
};


/* GET arch listing. */
router.get('/', function(req, res, next) {
  res.render('arch', { title: 'arch OS'})
});

router.post('/api/submit',function(req,res,next){
  create(req,res).then(v=>
    console.log(v)
  );
});

router.get('/api/getList',function(req,res,next){
  getAvailable(req,res).then(v=>{
    var tmpStr=JSON.stringify(v,null,2);
    const packJson = JSON.parse(tmpStr);
    // console.log(packJson)
      //1 - wait to compile
      //2 - compiling
      //3 - compiled
    for (var i in packJson){
      console.log(packJson[i])
      if(packJson[i]['state']==1){
        packJson[i]['state']='Waiting to Compile...'
      }else if(packJson[i]['state']==2){
        packJson[i]['state']='Compiling...'
      }else{
        packJson[i]['state']='Available'
      }
    }
    packJson.sort((a,b)=>a['name']-b['name'])
    res.send(packJson)
  });
});

module.exports = router;
