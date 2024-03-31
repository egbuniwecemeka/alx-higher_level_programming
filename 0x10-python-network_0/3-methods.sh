#!/bin/bash
# A bash script that list the HTTP Methods supported by a browser
curl -sI -X OPTIONS "$1"
