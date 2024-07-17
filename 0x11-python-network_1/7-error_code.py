#!/usr/bin/python3

""" 
    A python script taking a URL, handles HTTP error through the status code
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    status = response.status_code
    if status >= 400:
        print(f'Error code: {status}')
    else:
        print(response.text)
