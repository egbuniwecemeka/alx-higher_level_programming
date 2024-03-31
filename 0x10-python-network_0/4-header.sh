#!/bin/bash
# Script accepts a URL, sends a GET request and displays the body's response
curl -sHX "X-School-User-Id:98" GET "$1"
