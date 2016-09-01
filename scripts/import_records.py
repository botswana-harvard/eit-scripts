"""This is a script that is used to restore Redcap database backups."""

import os
import csv
import json
from unipath import Path
from datetime import datetime
from requests import post

# change file name to use backupup that is to be restored
#file = open('export_test.json', 'r')
file = open(os.path.join(Path(os.path.dirname(os.path.realpath(__file__))).ancestor(2).child('etc'), 'export_test'), 'r')
lines = json.load(file)
URL = 'https://redcap.sph.harvard.edu/redcap/api/'
data = []

# Insert Token here
TOKEN = ''

def main():        
    #response = post(URL, data=payload)
    payload = {'token': TOKEN, 'format': 'json', 'content': 'record'}
    response = post(URL, data=payload)
    print('Connection Status: {}'.format(response.status_code))
    payload['data'] = json.dumps(lines, separators=(',', ':'))
    response = post(URL, data=payload)
    print('Connection Status: {}'.format(response.status_code))
    print(response.text)

#        print('Completed running script')        

if __name__ == '__main__':
   main()
