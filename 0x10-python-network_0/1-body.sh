#!/bin/bash

# Use curl to send a GET request and display the body if the response status code is 200
curl -sL -X GET $1
