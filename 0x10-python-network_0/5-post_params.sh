#!/bin/bash
# Takes a URL, sends POST request and display the response body
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
