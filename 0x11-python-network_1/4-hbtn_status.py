#!/usr/bin/python3
"""
Fetches content from a URL using the requests package.
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text).__name__))
    print("\t- content: {}".format(response.text))
