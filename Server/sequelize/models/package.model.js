const { DataTypes } = require('sequelize');

module.exports = (sequelize) => {
	sequelize.define('package', {
		// The following specification of the 'id' attribute could be omitted
		// since it is the default.
        name:{
            allowNull: false,
            primaryKey: true,
			type: DataTypes.STRING
        },
        addr:{
            allowNull: false,
            type: DataTypes.STRING,
            validate:{
                isUrl: true, 
            }
        },
        state:{
            allowNull: false,
            type: DataTypes.INTEGER,
            validate:{
                isInt: true,
                min: 0,
                max: 3,
            }
        },
        email:{
            allowNull: true,
            type: DataTypes.STRING,
            validate:{
                isEmail: true,
            }
        }
	},{
        timestamps: false,
        freezeTableName: true
    });
};
