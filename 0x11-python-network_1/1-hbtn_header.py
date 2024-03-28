#!/usr/bin/python3
"""
    Python scripts that sends a request to an URL and retrieves Header X-Request-Id value 

"""

import sys
import urllib.request

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    x_req_id = response.headers.get('X-Request-Id')
    print(x_req_id)
