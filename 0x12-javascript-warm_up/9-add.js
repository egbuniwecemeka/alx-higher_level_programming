#!/usr/bin/node
const {argv} = require('node:process');

function add(a, b) {
  let sum = 0;
  sum = Number(a) + Number(b);
  console.log(sum);
}

add(argv[2], argv[3]);
