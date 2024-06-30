#!/usr/bin/node


function addMeMaybe(number, theFunction) {
	return theFunction(++number);
}

exports.addMeMaybe = addMeMaybe;
