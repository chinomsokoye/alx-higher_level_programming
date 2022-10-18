#!/usr/bin/node
// Print the number of movies where the character "Wedge Antilles" is present

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const i in results) {
      for (const charc of results[i].characters) {
        if (charc.search('/18/') > 0) { count += 1; }
      }
    }
    console.log(count);
  }
});
