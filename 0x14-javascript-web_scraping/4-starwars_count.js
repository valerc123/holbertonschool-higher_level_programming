#!/usr/bin/node

const url = process.argv[2];
const req = require('request');

req(url, (err, req, body) => {
  if (err) console.log(err);

  let res = JSON.parse(body).results;
  let wedge = 0;
  for (let index in res) {
    let character = res[index].characters;
    for (let i in character) {
      if (character[i].includes('18')) {
        wedge++;
      }
    }
  }
  console.log(wedge);
});
