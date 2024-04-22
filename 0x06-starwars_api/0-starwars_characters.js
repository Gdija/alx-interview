#!/usr/bin/node
const request = require('request');

function getMovieChar (movieId) {
  const Url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
  request(Url, (error, response, body) => {
    if (error) {
      console.error('Error :', error);
      return;
    }
    const jsonData = JSON.parse(body);
    const characters = jsonData.characters;
    const index = 0;

    function charById (index) {
      if (index >= characters.length) {
        return;
      }
      const characterUrl = characters[index];
      request(characterUrl, (charError, charResponse, charBody) => {
        if (charError) {
          console.error('Error:', charError);
        } else {
          const charData = JSON.parse(charBody);
          console.log(`${charData.name}`);
          charById(index + 1);
        }
      });
    }
    charById(index);
  });
}
const movieId = process.argv[2];
getMovieChar(movieId);
