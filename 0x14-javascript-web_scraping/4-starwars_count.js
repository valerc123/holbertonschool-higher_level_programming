#!/usr/bin/node

const url = process.argv[2];
const req = require('request');

req(url, (err, req, body) => {
  if (err) console.log(err);

  const res = JSON.parse(body).results;
  let wedge = 0;
  for (const index in res) {
    const character = res[index].characters;
    for (const i in character) {
      if (character[i].includes('18')) {
        wedge++;
      }
    }
  }
  console.log(wedge);
});
