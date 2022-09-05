#!/usr/bin/node
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  let size = 0;
  while (size < x) {
    console.log('X'.repeat(x));
    size++;
  }
}
