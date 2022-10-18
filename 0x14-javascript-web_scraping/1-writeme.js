#!/usr/bin/node
// Writes a string to a file

const fs = require('fs');
const file = process.argv[2];
const _write = process.argv[3];

fs.writeFile(file, _write, 'utf-8', function (error) {
  if (error) {
    console.log(error);
  }
});
