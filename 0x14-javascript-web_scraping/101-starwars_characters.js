#!/usr/bin/node
// Prints all characters of a Star Wars movie
const request = require('request');
const addr = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

function printCharacters (characters, idx) {
  request(characters[idx], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      if (idx + 1 < characters.length) {
        printCharacters(characters, idx + 1);
      }
    }
  });
}

request(addr, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
