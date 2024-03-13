#!/usr/bin/node
const { argv } = require('node:process');

function factorial (n) {
  if (isNaN(n) || n === 0) {
    return (1);
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(Number(argv[2])));
