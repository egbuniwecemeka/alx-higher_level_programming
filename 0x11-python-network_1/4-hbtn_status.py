#!/usr/bin/python3

""" A python script that fetches a request from a URL """

import requests

if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print(f"""Body response:
            \t - type: {type(req)}
            \t - content: {req.text}""")
