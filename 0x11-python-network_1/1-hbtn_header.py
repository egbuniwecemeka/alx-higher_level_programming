#!/usr/bin/python3
"""
    Python scripts that sends a request to an URL and retrieves Header X-Request-Id value 

"""

import sys
import urllib.request

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    x_req_id = response.getheader('X-Request-Id')
    print(x_req_id)
