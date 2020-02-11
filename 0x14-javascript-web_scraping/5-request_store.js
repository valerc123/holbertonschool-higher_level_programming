#!/usr/bin/node

const req = require('request');
const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');

req(url, (err, res, body) => {
  if (err) console.log(err);
  fs.writeFile(file, JSON.stringify(body), 'utf-8', (err) => {
    if (err) console.log(err);
  });
});
