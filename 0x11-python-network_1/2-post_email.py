#!/usr/bin/python3

"""
    A python script that takes a URl and email as arguments,
    passing the email are aprameter to the URL
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        html = response.read()
        print(html.decode('utf8'))
