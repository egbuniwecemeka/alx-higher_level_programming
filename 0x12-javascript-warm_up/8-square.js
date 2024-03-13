#!/usr/bin/node
const { argv } = require('node:process');

if (argv[2] === undefined || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const x = Number(argv[2]);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
