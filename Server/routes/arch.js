var express = require('express');
var router = express.Router();

const { models } = require('../sequelize');


async function getAll(req, res) {
	const packages = await models.package.findAll();
  return packages
};


async function create(req, res) {
  let item = req.body
  // item.push({
  //   'state':0
  // })
  console.log(item)
  await models.package.create(item);
};


/* GET arch listing. */
router.get('/', function(req, res, next) {

  getAll(req,res).then(v=>
    res.render('arch', { title: 'arch OS',data:v })
  );
  
});

router.post('/api/submit',function(req,res,next){
  create(req,res).then(v=>
    console.log(v),
    res.status(201).send('success')
  );
});

module.exports = router;

// async function getAll(req, res) {
// 	const packages = await models.package.findAll();
// 	res.status(200).json(packages);
// };
// async function create(req, res) {
// 	await models.package.create(req.body);
// 	res.status(201).end();
// };
