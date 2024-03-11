#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length === undefined) {
  console.log('No argument');
} else if (argv.length >= 3) {
  console.log(argv[2]);
}
