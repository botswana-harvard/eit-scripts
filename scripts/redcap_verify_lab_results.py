"""Cater for NOT RESULT but received"""

import os
import csv
from unipath import Path
from django.db import models

def verify_lab_results():
    #file = open('check.csv')
    #specimen_errors = open('Incorrect Enrolled Specimen Identifiers.csv', 'w')
    file = open(os.path.join(Path(os.path.dirname(os.path.realpath(__file__))).ancestor(2).child('etc'), 'check.csv'), 'r')
    specimen_errors = open(os.path.join(Path(os.path.dirname(os.path.realpath(__file__))).ancestor(2).child('etc'), 'Incorrect Enrolled Specimen Identifiers.csv'), 'w')
    to_file = csv.writer(specimen_errors)
    lines = csv.reader(file)
    model = models.get_model('lab_result','Result')
    error = []
    
    for row in lines:
        try:
            result = model.objects.using('lab_api').get(receive_identifier=row[2].strip())
            
        except Result.DoesNotExist:
            if row[2] != '':
                print (row[0] + " "+ row[1]+ " " + row[2])
                error.append([row[0], row[1], row[2]])
    
    to_file.writerows(error)  
    specimen_errors.close()
verify_lab_results()
    
def verify_screening_results():
    #file = open('screen_results.csv')
    #specimen_errors = open('Incorrect Screening Specimen Identifiers.csv', 'w')
    file = open(os.path.join(Path(os.path.dirname(os.path.realpath(__file__))).ancestor(2).child('etc'), 'screen_results.csv'), 'r')
    specimen_errors = open(os.path.join(Path(os.path.dirname(os.path.realpath(__file__))).ancestor(2).child('etc'), 'Incorrect Screening Specimen Identifiers.csv'), 'w')
    to_file = csv.writer(specimen_errors)
    lines = csv.reader(file)
    model = models.get_model('lab_result','Result')
    error = []
    
    for row in lines:
        try:
            result = model.objects.using('lab_api').get(receive_identifier=row[10].strip())  
        except Result.DoesNotExist:
            if row[10] != '':
                print (row[0] + " "+ row[1]+ " " + row[10])
                error.append([row[0], row[1], row[10]])
    
    to_file.writerows(error)  
    specimen_errors.close()
    
verify_screening_results()
