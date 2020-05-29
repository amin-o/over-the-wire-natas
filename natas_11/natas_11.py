#!/usr/bin/env python

import requests
import re
import urllib.parse
import subprocess

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = 'http://natas11.natas.labs.overthewire.org'

req = requests.get(url, auth = (username, password))

#get cookie data
data = req.cookies['data']

#decode url
decoded = urllib.parse.unquote(data)

#call php script
secret = subprocess.check_output('php level_11.php "' + decoded + '"', shell=True)
secretDecoded = secret.decode('utf-8')

req = requests.post(url, auth=(username, password), cookies={'data' : secretDecoded})

print(re.findall('he password for natas12 is (.*?)<br>', req.text)[0])