#!/usr/bin/node

const myArgs = process.argv;

if (myArgs.length === 2) {
  console.log('No argument');
} else if (myArgs.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
console.log(myArgs)