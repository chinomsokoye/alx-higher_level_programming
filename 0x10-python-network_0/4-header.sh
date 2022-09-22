#!/bin/bash
# Take URL, send GET request and displays body of response
curl -s "$1" -X GET -H "X-School-User-Id: 98"
