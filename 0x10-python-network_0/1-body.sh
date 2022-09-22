#!/bin/bash
# Take in URL, sends GET request and display body of response
curl -s "$1" -X GET -L
