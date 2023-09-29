#!/bin/bash
# Send a request to a URL and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
