#!/usr/bin/node
// Reads and prints the content of a file

const file = process.argv[2];
const fs = require('fs');

fs.readFile(file, 'utf-8', (error, data) => {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
