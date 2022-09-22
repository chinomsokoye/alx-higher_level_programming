#!/bin/bash
# Make a request, cause the server to respond with a message, in response body
curl -sX PUT -L -d "user_id=98" -H "Origin:HolbertonSchool" "0.0.0.0:5000/catch_me"
