#!/usr/bin/node
// Print all characters of a star wars movie
const request = require('request');
const url = 'https://swapi.co/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).characters;
    for (const i of results) {
      request(i, (a, b, c) => console.log(JSON.parse(c).name));
    }
  }
});
