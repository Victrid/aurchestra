var config = {
    dbname: 'testdb',
    uname: 'floudk',
    upwd: '918918',
    host: 'localhost',
    port: 3306,
    dialect: 'mysql',
    pool: {
      max: 5,
      min: 0,
      idle: 10000
    }
  };
  
  module.exports = config;