#!/usr/bin/node
/* prints the title of a Star Wars movie where the episode number
 * matches a given integer
*/
const request = require('request');

const episodeNo = process.argv[2];

const baseUrl = `https://swapi-api.alx-tools.com/api/${episodeNo}`;

request(baseUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const movieData = JSON.parse(body).title;
  console.log(movieData);
});
