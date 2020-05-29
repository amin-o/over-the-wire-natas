#!/usr/bin/env python

import requests
import re

url='https://overthewire.org/wargames/natas/natas0.html'

req = requests.get(url)

username = re.findall('Username: (.*)',req.text)[0]
password = re.findall('Password: (.*)',req.text)[0]

url='http://natas0.natas.labs.overthewire.org'

req = requests.post(url, auth=(username,password))

print(re.findall('<!--The password for natas1 is (.*)-->', req.text)[0])
