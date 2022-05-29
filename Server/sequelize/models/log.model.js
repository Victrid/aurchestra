const { DataTypes } = require('sequelize');
// import bcrypt from 'bcrypt-nodejs'
//Export a function that defines the model
module.exports = (sequelize) => {
	sequelize.define('loginfo', {
		// The following specification of the 'id' attribute could be omitted
		// since it is the default.
		id: {
			type: DataTypes.INTEGER,
			primaryKey: true,
            autoIncrement:true,
		},
        name:{
            allowNull: true,
            type: DataTypes.STRING,
        },
        loginfo:{
            allowNull: true,
            type: DataTypes.TEXT,
        }
	},{
        timestamps: false,
        freezeTableName: true
    });
};
