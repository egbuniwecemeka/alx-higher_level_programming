#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length === undefined) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}
