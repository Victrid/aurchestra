const { DataTypes } = require('sequelize');
// import bcrypt from 'bcrypt-nodejs'
//Export a function that defines the model
module.exports = (sequelize) => {
	sequelize.define('admin', {
		// The following specification of the 'id' attribute could be omitted
		// since it is the default.
		username: {
			allowNull: false,
			type: DataTypes.STRING,
			primaryKey: true,
			validate: {
				// We require usernames to have length of at least 3, and
				// only use letters, numbers and underscores.
			}
		},
        password:{
            allowNull: false,
            type: DataTypes.STRING,
            
        }
	},{
        // instanceMethods: {
        //     generateHash(password) {
        //         return bcrypt.hash(password, bcrypt.genSaltSync(8));
        //     },
        //     validPassword(password) {
        //         return bcrypt.compare(password, this.password);
        //     }
        // },
        timestamps: false,
        freezeTableName: true
    });
};
