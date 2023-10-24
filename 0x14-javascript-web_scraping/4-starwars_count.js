#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;
let count = 0;

request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    data.results.forEach((movie) => {
      if (movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count += 1;
      }
    });
    console.log(count);
  } else {
    console.error(error);
  }
});
