#!/usr/bin/env python
import requests
import re
import subprocess

print('1 - Run full process.')
print('2 - Just get the flag.')
switch = input()

url='http://natas3.natas.labs.overthewire.org'
 
username = 'natas3'
password = 'sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14' 

if(switch == '1'):

    subprocess.call(['sh_scripts/level_3_gobuster.sh'])

    req = requests.post(url + '/robots.txt', auth=(username,password))
    print(req.text)


req = requests.post(url + '/s3cr3t/users.txt', auth=(username,password))
print(re.findall('natas4:(.*)',req.text)[0])

