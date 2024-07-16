#!/usr/bin/python3

from urllib.request import Request, urlopen
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
