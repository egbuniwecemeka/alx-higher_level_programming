#!/usr/bin/node
let ncount = 0;
exports.logMe = function (item) {
  console.log(ncount + ': ' + item);
  ncount++;
};
