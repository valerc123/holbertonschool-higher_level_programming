#!/usr/bin/node

const url = process.argv[2];
const req = require('request');

req(url, (err, res, body) => {
  if (err) console.log(err);
  let count = 0;
  const taskCompleted = {};
  const obj = JSON.parse(body);
  for (const i in obj) {
    const userID = obj[i].userId;
    const task = obj[i].completed;
    if (task) {
      count++;
      taskCompleted[userID] = count;
    }
  }
  console.log(taskCompleted);
});
