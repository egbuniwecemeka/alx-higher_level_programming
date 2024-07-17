#!/usr/bin/python3

""" A python script that retrieves a specific header from a response """

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    header = req.headers['X-Request-Id']
    print(header)
