const sequelize = require('../sequelize');
async function initial(){
    console.log('Initial the SQLite to serve for web about login and package states...');
    await sequelize.sync({ force: true });
    await sequelize.models.admin.bulkCreate([
        {username:'admin',password:'admin'},
    ]);
    await sequelize.models.package.bulkCreate([
        {name:'admin',addr:'admin',state:1,email:"111@qq.com"},
    ]);
    console.log('SQLite initial success!');
}
initial();