#!/usr/bin/python3 

import requests
import re
import hashlib


url="http://94.237.53.58:53047/"

#step 1 - get the string


session = requests.session()

r = session.get(url)
html = r.text
match = re.search("[a-zA-Z0-9]{20}",html)

#step -2 encrypt with md5

string = match.group()
hash = hashlib.md5(string.encode("utf")).hexdigest()

#step - Post hast to web

p = session.post(url, data={"hash":hash})
print(p.text)