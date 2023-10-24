#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const charactersUrls = JSON.parse(body).characters;

    const getCharacterName = (url) => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (!error && response.statusCode === 200) {
            const character = JSON.parse(body);
            resolve(character.name);
          } else {
            reject(error);
          }
        });
      });
    };

    const getCharacters = charactersUrls.map((characterUrl) =>
      getCharacterName(characterUrl)
    );

    Promise.all(getCharacters)
      .then((names) => {
        names.forEach((name) => {
          console.log(name);
        });
      })
      .catch((error) => {
        console.error(error);
      });
  } else {
    console.error(error);
  }
});
