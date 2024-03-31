#!/bin/bash
# A bash script that list the HTTP Methods supported by a browser
curl -s -i -X OPTIONS "$1" | awk '/Allow:/ {print "Supported HTTP Methods:", $2}'
