#!/bin/bash
# Use `curl` to display all HTTP methods the server will accept
curl -sI "$1" | awk '/^Allow/{$1=""; print "\b"$0}'
