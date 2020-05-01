#!/usr/bin/bash
 
url='http://natas3.natas.labs.overthewire.org'

username='natas3'
password='sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'

#edit the wordlist path
wordlist_path='/usr/share/wordlists/dirb-master/common.txt'

gobuster dir -P $password -U $username -u $url -w $wordlist_path

