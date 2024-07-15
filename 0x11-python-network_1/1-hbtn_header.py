#!/usr/bin/python3
"""
    Script sends a request to an URL & retrieves Header X-Request-Id value

"""

import sys
import urllib.request

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    html = response.getheader('X-Request-Id')
    print(html)
