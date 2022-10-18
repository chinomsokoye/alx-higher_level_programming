#!/usr/bin/node
// Print the number of movies where the character "Wedge Antilles" is present

const args = process.argv;
const requestUrl = args[2];
const request = require('request');
request(requestUrl, function (error, response, body) {
  if (error) {
    console.log('error:', error); // Outputs error if occur
  } else {
    const jsons = JSON.parse(body);
    const result = jsons.result;
    let counter = 0;
    for (let i = 0; i < result.length; i++) {
	  const charc = (result[i].characters);
	  for (let j = 0; j < charc.length; j++) {
	      const checks = charc[j].endsWith('18/');
	      if (checks) {
		  counter++;
	      }
	  }
    }
    console.log(counter);
  }
});
