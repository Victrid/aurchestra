const { DataTypes } = require('sequelize');
const moment =require('moment') ;

module.exports = (sequelize) => {
	sequelize.define('softwareinfo', {
		// The following specification of the 'id' attribute could be omitted
		// since it is the default.
        name:{
            allowNull: false,
            primaryKey: true,
			type: DataTypes.STRING
        },
        address:{
            allowNull: false,
            type: DataTypes.STRING,
        },
        state:{
            allowNull: false,
            type: DataTypes.INTEGER,
            validate:{
                isInt: true,
                min: 0,
                max: 7,
            }
        },
        email:{
            allowNull: true,
            type: DataTypes.STRING,
            validate:{
                isEmail: true,
            }
        },
        lastupdatetime:{
            allowNull:true,
            type: DataTypes.DATE,
            get(){
                if(this.getDataValue('lastupdatetime')){
                    return moment(this.getDataValue('lastupdatetime')).format('YYYY/DD/MM h:mm');   
                }else{
                    return '---'
                }
            }
        }
	},{
        timestamps: false,
        freezeTableName: true
    });
};
