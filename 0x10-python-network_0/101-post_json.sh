#!/bin/bash
# Send a JSON POST request to URL, display body of response
curl -s -X POST "$1" -H "Content-Type: application/json" -d @"$2"
