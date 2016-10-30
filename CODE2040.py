import requests
import json


token = '161fdc48632480b96fa68fe9abf8c8cd'
github = 'ttps://github.com/AngieW/Code2040'

payloadd = {'token': token, 'github': github}

request = requests.post('http://challenge.code2040.org/api/register', params=payloadd)