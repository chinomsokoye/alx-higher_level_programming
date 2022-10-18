#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = {};
    for (const todo of JSON.parse(body)) {
      if (todo.completed) {
        if (results[todo.userId] === undefined) { results[todo.userId] = 0; }
        results[todo.userId] += 1;
      }
    }
    console.log(results);
  }
});
