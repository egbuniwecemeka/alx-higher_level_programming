#!/usr/bin/node
const { argv } = require('node:process');

if (isNaN(argv[2]) || argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log('My number:', parseInt(argv[2]));
}
