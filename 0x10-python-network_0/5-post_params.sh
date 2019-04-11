#!/bin/bash
# Use `curl` to `POST` `email` & `subject` parameters, and display the body of the response
curl -sX POST -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD' "$1"
