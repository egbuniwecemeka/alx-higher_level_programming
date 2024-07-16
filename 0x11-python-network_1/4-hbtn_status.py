#!/usr/bin/python3

""" A python script that fetches a request from a URL """

import requests

if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"Body response:\n"
        f"\t - type: {type(req.text)}\n"
        f"\t - content: {req.text}")
