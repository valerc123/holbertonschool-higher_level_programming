#!/usr/bin/node

const url = process.argv[2];
const req = require('request');

req(url, (err, res, body) => {
  if (err) console.log(err);
  const taskCompleted = {};
  const obj = JSON.parse(body);
  for (const i in obj) {
    const task = obj[i];
    const userID = obj[i].userId;

    if (task.completed === true) {
      if (taskCompleted[userID] === undefined) {
        taskCompleted[userID] = 1;
      } else {
        taskCompleted[userID] += 1;
      }
    }
  }
  console.log(taskCompleted);
});
