#!/usr/bin/node

const myArgs = process.argv;

if (isNaN(parseInt(myArgs[2]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(myArgs[2]));
}
