#!/bin/bash
# A bash script that list the HTTP Methods supported by a protocol
curl -sI "$1" | grep "Allow" | cut -d' ' -f2-
