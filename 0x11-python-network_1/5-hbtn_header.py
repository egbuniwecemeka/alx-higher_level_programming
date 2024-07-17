#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    url = sys.argv
    req = requests.get(url)
    print(req.getheader('X-Request-Id'))
