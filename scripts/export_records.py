import csv
from datetime import datetime
import json
from requests import post

file = open('token.txt', 'r')
lines = file.readlines()

URL = 'https://redcap.sph.harvard.edu/redcap/api/'


def main(): 
    for line in lines:
        # Get the token form file
        db,token=line.split('=')

        TOKEN = token.strip()
        payload = {'token': TOKEN, 'format': 'json', 'content': 'metadata'}
        data = []
        header = []
        
        response = post(URL, data=payload)
        print('Connection Status: {}'.format(response.status_code))
        metadata = response.json()
        # Get the field names
        #for _ in metadata:
        #    print(_.get('field_name'))
        #    header.append(_.get('field_name'))
        #data.append(['This project has {} fields'.format(len(metadata))])
        #data.append(header)
        print('This project has {} fields'.format(len(metadata)))
        # Get the data
        payload['content'] = 'record'
        payload['type'] = 'flat'
        response = post(URL, data=payload)
        records = response.json()
        with open("export_{}_{}.json".format( db, datetime.today()), "w") as outfile:
            json.dump(records, outfile, indent=4)
        print(response.status_code)
        

if __name__ == '__main__':
   main()
