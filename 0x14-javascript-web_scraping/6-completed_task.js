#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const args = process.argv;
const reqURL = args[2];
const request = require('request');
request(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const todos = JSON.parse(body);
    const dash = {};
    for (let i = 0; i < todos.length; i++) {
      const status = (todos[i].completed);
      const key = todos[i].userId.toString();
      if (status) {
        if (dash[key]) {
          dash[key]++;
        } else {
          dash[key] = 1;
        }
      }
    }
    console.log(dash);
  }
});
