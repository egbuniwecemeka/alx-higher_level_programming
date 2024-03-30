#!/bin/bash
# A bash script that takes in a URL, sends a request to that URL,
echo curl -sI "$1" -o - | wc -c
