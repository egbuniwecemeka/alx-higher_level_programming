#!/usr/bin/node
const { argv } = require('node:process');

if (process.argv.length === 0) { console.log('No argument'); } else if (process.argv.length === 1) { console.log('Argument found'); } else { console.log('Arguments found'); }
