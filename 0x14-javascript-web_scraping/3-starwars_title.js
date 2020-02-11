#!/usr/bin/node

const req = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

req(url, (err, req, body) => {
  if (err) console.log(err);
  console.log(JSON.parse(body).title);
});
