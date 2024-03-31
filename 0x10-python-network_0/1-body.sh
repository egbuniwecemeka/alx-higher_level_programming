#!/bin/bash
# A bash script that takes in a URL, sends a request to that URL,
echo -n $(curl -sL "$1")
