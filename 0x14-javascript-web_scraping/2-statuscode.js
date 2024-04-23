#!/usr/bin/node
/* a script that display the status code of a GET request. */
const req = require("request");

const base_url = process.argv[2];

req.get(base_url, (err, res) => {
  if (err) {
    console.error(err);
  }
  console.log('code: res.statusCode');
})
