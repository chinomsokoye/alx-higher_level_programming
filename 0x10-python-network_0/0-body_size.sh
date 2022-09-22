#!/bin/bash
# Takes in URL, sends a request and display size of the response body
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
