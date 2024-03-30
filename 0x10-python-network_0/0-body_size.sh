#!/bin/bash
# A bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
# Display size in bytes

if [ $# -ne 1 ]; then
	echo "Useage: $0 <URL>"
fi

url=$1

body_size=$(curl -s "$1" | wc -c)

echo "$body_size" 
