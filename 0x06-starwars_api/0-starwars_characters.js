#!/usr/bin/node
const request = require('request');

function getMovieChar(movieId) {
	const Url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
	request(Url, (error, response, body) => {
		if (error) {
			console.error('Error :', error);
			return;
		}
		const jsonData = JSON.parse(body);
		const characters = jsonData.characters;

		characters.forEach((characterUrl) => {
			request(characterUrl, (charError, charResponse, charBody) => {
				if(charError) {
					console.error('Error:',charError);
					return;
				}
				const charData = JSON.parse(charBody);
				console.log(`${charData.name}`);
			});
		});
});
}
const movieId = process.argv[2];
getMovieChar(movieId);
