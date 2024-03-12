#!/usr/bin/node
exports.nbOccurrences = function (list, searchElement) {
  let occurrs = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      occurrs++;
    }
  }
  return (occurrs);
};
