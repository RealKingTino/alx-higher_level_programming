#!/bin/bash
# Use curl to send a GET request and display the body 
response=$(curl -sL -w "%{http_code}" -X GET "$1")

# Check if the response status code is 200 and display the body if it is
if [ "$response" -eq 200 ];
then
	curl -sL -X GET "$1"
fi
