#!/usr/bin/node
require('request').get(process.argv[2], (err, resp, body) => {
  if (err) {
    console.log(err);
  } else {
    let tasks = JSON.parse(body);
    let resp = {};
    for (let i = 0; i < tasks.length; i++) {
      if (tasks[i].completed) {
        if (!(tasks[i].userId in resp)) {
          resp[tasks[i].userId] = 0;
        }
        resp[tasks[i].userId] += 1;
      }
    }
    console.log(resp);
  }
});
