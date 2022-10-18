#!/usr/bin/node
// A script that prints the number of movies where the character Wedge Antilles is present

const args = process.argv;
const reqURL = args[2];
const request = require('request');
request(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error); // Print the error if one occurred
  } else {
    const jso = JSON.parse(body);
    const results = jso.results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      const chars = (results[i].characters);
      for (let j = 0; j < chars.length; j++) {
        const check18 = chars[j].endsWith('18/');
        if (check18) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
