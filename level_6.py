#!/usr/bin/env python
import requests
import re

url='http://natas6.natas.labs.overthewire.org'
 
username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1' 

req = requests.post(url, auth=(username,password), data = {'secret': 'FOEIUWGHFEEUHOFUOIU', 'submit': 'submit'})

print(re.findall('natas7 is (.*)', req.text)[0])