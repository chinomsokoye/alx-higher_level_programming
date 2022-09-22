#!/bin/bash
# Send request to URL, display only status code of response
curl -sI -w '%{response_code}' "$1" -o /dev/null
