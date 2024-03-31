#!/bin/bash
# Script takes URL as input, sends a POST request and display body's response
curl -sXH POST "email:test@gmail.com" "subject: I will always be here for PLD" "$1"
