#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL
and displays the value of the X-Request-Id
variable found in the header of the response
"""

import urllib.request
import sys

from requests import request

url = sys.argv[1]
request = urllib.request.Request(url)
with urllib.request.urlopen(request) as response:
    print(dict(response.headers).get("X-Request-Id"))
