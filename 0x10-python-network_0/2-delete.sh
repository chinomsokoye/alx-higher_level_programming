#!/bin/bash
# Send DELETE request to URL, passed as argument and display response body
curl -s "$1" -X DELETE
