#!/usr/bin/python3

"""
    Python script taking a CML argument (URL) sends a request to the URL
    Displays the body of the URL in utf-8
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            res = response.read()
            print(res.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
