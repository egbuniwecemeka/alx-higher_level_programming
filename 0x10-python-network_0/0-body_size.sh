#!/bin/bash
# A bash script that takes in a URL, sends a request to that URL,
echo $(curl -s "$1" | wc -c)
