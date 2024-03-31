#!/bin/bash
# A bash script that takes in a URL, sends a request to that URL,
echo "$(curl -s -w "%{http_code}" "$1" | { read -r status_code; echo "$status_code"; })"
