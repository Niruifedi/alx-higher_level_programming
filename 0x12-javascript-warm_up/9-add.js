#!/usr/bin/node

const x = process.argv[2];
const y = process.argv[3];

function add (a, b) {
  const first = parseInt(a);
  const second = parseInt(b);
  return first + second;
}
const res = add(x, y);
console.log(res);
