#!/usr/bin/env python

import requests
import re

url='http://natas1.natas.labs.overthewire.org'
 
username = "natas1"
password = "gtVrDuiDfck831PqWsLEZy5gyDz1clto" 

req = requests.post(url, auth=(username,password))

print(re.findall('<!--The password for natas2 is (.*)-->', req.text)[0])