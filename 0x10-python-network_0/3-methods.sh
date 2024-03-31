#!/bin/bash
# A bash script that list the HTTP Methods supported by a browser
curl -sIX OPTIONS "$1"
