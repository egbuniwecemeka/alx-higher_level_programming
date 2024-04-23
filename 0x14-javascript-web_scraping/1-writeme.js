#!/usr/bin/node
/*  a script that writes a string to a file. */
const fs = require('fs');

const filePath = process.argv[2];

const fwrite = process.argv[3];

fs.writeFile(filePath, fwrite, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
});
