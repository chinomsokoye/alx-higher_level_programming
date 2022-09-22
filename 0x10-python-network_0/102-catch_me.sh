#!/bin/bash
# Make a request, cause the server to respond with a message, in response body
curl -s 0.0.0.0:5000/catch_me -X PUT -L -d -H "Origin: You got me!"
