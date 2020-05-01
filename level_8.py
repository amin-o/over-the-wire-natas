#!/usr/bin/env python
import requests
import re
import base64

url='http://natas8.natas.labs.overthewire.org'
 
username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe' 

req = requests.get(url + '/index-source.html', auth=(username,password))

encodedSecret = re.findall('3d.*62',req.text)[0]

encodedSecretToAscii = bytes.fromhex(encodedSecret).decode('utf-8')

encodedSecretReversed = encodedSecretToAscii[::-1]

print(base64.b64decode(encodedSecretReversed).decode('utf-8'))