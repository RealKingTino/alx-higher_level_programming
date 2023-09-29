#!/usr/bin/python3
"""
Sends a POST request to a URL with an email parameter
and displays the response body.
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    data = urllib.parse.urlencode(data).encode("ascii")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
