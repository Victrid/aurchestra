// file for common helper functions


//assert the request ID param is valid
// and convert string to a number 
function getIdParam(req) {
	const id = req.params.id;
	if (/^\d+$/.test(id)) {
		return Number.parseInt(id, 10);
	}
	throw new TypeError(`Invalid ':id' param: "${id}"`);
}

module.exports = { getIdParam };