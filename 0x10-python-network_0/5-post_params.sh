#!/bin/bash
# Script takes URL as input, sends a POST request and display body's response
curl -s -X POST -H "email:test@gmail.com" -H "subject: I will always be here for PLD" "$1"
