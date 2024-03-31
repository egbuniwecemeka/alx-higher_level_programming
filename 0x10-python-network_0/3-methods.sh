#!/bin/bash
# A bash script that list the HTTP Methods supported by a browser
curl -sX OPTIONS "$1"
