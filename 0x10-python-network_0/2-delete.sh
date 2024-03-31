#!/bin/bash
# A bash script that uses a DELETE req and displays the body.
curl -sX DELETE "$1" | echo -n "I'm a DELETE request"
