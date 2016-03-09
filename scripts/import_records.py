import csv
import json
from datetime import datetime
from requests import post

file = open('export_TEST_2016-03-08 10:58:46-953057.json', 'r')
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
