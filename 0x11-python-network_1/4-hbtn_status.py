#!/usr/bin/python3
"""
Fetches content from a URL using the requests package.
"""


if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(response.text.__class__))
    print("\t- content: {}".format(response.text))
