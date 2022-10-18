#!/usr/bin/node
// Display the status code of a GET request

const args = process.argv;
const request = require('request');
request(args[2], function (error, response, body) {
  if (error) {
    console.log('error:', error); // Output error if occur
  } else console.log('code:', response && response.statusCode);
});
