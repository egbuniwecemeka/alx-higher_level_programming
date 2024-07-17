#!/usr/bin/python3

"""
    A python script that takes a letter as argument,
    sends a POST request to a URL
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    url = 'http://0.0.0.0:5000/search_user'

    response = requests.post(url, data={'q': q})

    try:
        """ Parse response to JSON """
        json = response.json()
        if json:
            print(f"[{json.get('id')}] {json.get('name')}")
        else:
            print('No result')
    except ValueError:
        """ if response not a valid JSON """
        print('Not a valid JSON')
