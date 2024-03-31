#!/bin/bash
# Script takes URL as input, sends a POST request and display body's response
curl -sX POST "$1" -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD"
