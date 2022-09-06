#!/usr/bin/node

const x = process.argv[2];

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < x; i++) {
    let msg = '';
    for (let j = 0; j < x; j++) {
      msg = msg + 'X';
    }
    console.log(msg);
  }
}
