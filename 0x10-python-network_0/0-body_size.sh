#!/usr/bin/env bash
# Use `curl` to displays the size of the body of the response
curl -sI $1 | awk '/^Content-Length/{print $2}'
