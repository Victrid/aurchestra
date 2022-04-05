const { Sequelize } = require('sequelize');
const { applyExtraSetup } = require('./extra-setup');
const config = require('../config/db.config');

const sequelize = new Sequelize(
    config.dbname,
    config.uname,
    config.upwd,
    {
        host: config.host,
        dialect: config.dialect,
        pool: config.pool
    }
);

const modelDefiners = [
	require('./models/admin.model'),
	require('./models/package.model'),
	// Add more models here...
	// require('./models/item'),
];

// We define all models according to their files.
for (const modelDefiner of modelDefiners) {
	modelDefiner(sequelize);
}

// We execute any extra setup after the models are defined, such as adding associations.
applyExtraSetup(sequelize);

// We export the sequelize connection instance to be used around our app.
module.exports = sequelize;