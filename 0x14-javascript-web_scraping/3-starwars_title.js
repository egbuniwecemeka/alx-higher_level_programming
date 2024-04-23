#!/usr/bin/node
/* prints the title of a Star Wars movie where the episode number
 * matches a given integer
*/
const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/:id';

const episodeNo = process.argv[2];

request.get(baseUrl, episodeNo,  (err, response) => {
  if (err) {
    console.error(err);
  }
  console.log(response);
})

