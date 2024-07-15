#!/usr/bin/python3

import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]

values = {'email': email}
data = urllib.parse.urlencode(values)
data = data.encode('ascii')
request = urllib.request.Request(url, data)
with urllib.request.urlopen(request) as response:
    html = response.read()
    print(html.decode('utf8'))
