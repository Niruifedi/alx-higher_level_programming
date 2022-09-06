#!/usr/bin/node

const times = 'C is fun';

const x = process.argv;

if (isNaN(parseInt(x[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x[2]; i++) {
    console.log(times);
  }
}
