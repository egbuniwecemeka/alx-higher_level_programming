#!/bin/bash
# A bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
# Display size in bytes

if [ $# -ne 0 ]; then
	echo "Useage: $0 <URL>"
fi

url=$1

response=$(curl -sI "$url" | awk '/Content-Length/ {print $2}')

echo "$response" | tr -d '\r' 
