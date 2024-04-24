#!/usr/bin/node

// import request module
const request = require('request');

// api url to fetch response from
const url = process.argv[2];

// Character ID used in filtering result
const wedge_ant = 18;

request(url, (err, response, body) => {
  // Error handling
  if (err) {
    console.error(err);
  }
  // 
  result = JSON.parse(body).result;
  // use reduce to iterate over movies in result array
  console.log(result.reduce((count, movie) => {
    return movie.characters.find((character) => character.endsWith('/18/'))
    // if character ID of 18 is found, increment
    ? count + 1
    // else display count
    : count
  }, 0));
});
