import csv
from django.db import models

def child_viral_load():
    """Ensure that the all the values of the child viral load match those in the lis."""
    file = open('child_viral_load_results.csv', 'r')
    specimen_errors = open('Incorrect Child Viral Load Result.csv', 'w')
    to_file = csv.writer(specimen_errors)
    lines = csv.reader(file)
    model = models.get_model('lab_result_item','ResultItem')
    error = []
    error.append(["Subject Identifier", "Event", "Specimen Identifier", "Redcap Value", "Value on LIS"])
    
    for row in lines:
        try:
            result_item = model.objects.using('lab_api').get(result__receive_identifier=row[3].strip())
            if result_item.test_code.code == 'AUVL':
                if row[19] != result_item.result_item_value:
                    print (row[19]+ " "+result_item.result_item_value)
                    error.append([row[0], row[1], row[3], row[19], result_item.result_item_value])
            else:
                print(result_item.test_code.code)
        except ResultItem.DoesNotExist:
            if row[3] != '':
                print (row[0] + " "+ row[1]+ " " + row[2])
                error.append([row[0], row[1], row[3]])
    
    to_file.writerows(error)  
    specimen_errors.close()
child_viral_load()


import csv
from django.db import models
def child_cd4():
    """Ensure that the all the values of the child CD4 match those in the lis."""
    file = open('child_cd4.csv')
    specimen_errors = open('Child CD4 Result Querry.csv', 'w')
    to_file = csv.writer(specimen_errors)
    lines = csv.reader(file)
    model = models.get_model('lab_result_item','ResultItem')
    error = []
    error.append(["Subject Identifier", "Event", "Specimen Identifier","Test Code", "Redcap Value", "Value on LIS"])
    spec_id = []
    
    for row in lines:
        try:
            items = model.objects.using('lab_api').filter(result__receive_identifier=row[2].strip())
            for result_item in items:
                if result_item.test_code.code == 'CD4':
                    if int(float(row[17].strip())) != int(float(result_item.result_item_value)):
                        print (row[17]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[17], result_item.result_item_value])
                elif result_item.test_code.code == 'CD4%':
                    if row[19].strip() != str(result_item.result_item_value):
                        print (row[19]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[19], result_item.result_item_value])
                elif result_item.test_code.code == 'CD8':
                    if int(float(row[23].strip())) != int(float(result_item.result_item_value)):
                        print (row[23]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[23], result_item.result_item_value])
                elif result_item.test_code.code == 'CD8%':
                    if row[21].strip() != str(result_item.result_item_value):
                        print (row[21]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[21], result_item.result_item_value])
                else:
                    print(result_item.test_code.code)
        except ResultItem.DoesNotExist:
            if row[2] != '':
                print (row[0] + " "+ row[1]+ " " + row[2])
                error.append([row[0], row[1], row[2], 'incorrect specimen id'])
    
    to_file.writerows(error)  
    specimen_errors.close()
child_cd4()


import csv
from django.db import models
def child_hematology():
    """Ensure that the all the values of the child Hematology match those in the lis."""
    file = open('child_hema.csv')
    specimen_errors = open('Child Hema Result Querry.csv', 'w')
    to_file = csv.writer(specimen_errors)
    lines = csv.reader(file)
    model = models.get_model('lab_result_item','ResultItem')
    error = []
    error.append(["Subject Identifier", "Event", "Specimen Identifier","Test Code", "Redcap Value", "Value on LIS"])
    spec_id = []
    
    for row in lines:
        try:
            items = model.objects.using('lab_api').filter(result__receive_identifier=row[2].strip())
            for result_item in items:
                if result_item.test_code.code == 'RBC':
                    if float(row[17].strip()) != float(result_item.result_item_value):
                        print (row[17]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[17], result_item.result_item_value])
                elif result_item.test_code.code == 'WBC':
                    if float(row[19].strip()) != float(result_item.result_item_value):
                        print (row[19]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[19], result_item.result_item_value])
                elif result_item.test_code.code == 'HGB':
                    if float(row[21].strip()) != float(result_item.result_item_value):
                        print (row[21]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[21], result_item.result_item_value])
                elif result_item.test_code.code == 'HCT':
                    if float(row[23].strip()) != float(result_item.result_item_value):
                        print (row[23]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[23], result_item.result_item_value])
                elif result_item.test_code.code == 'MCV':
                    if float(row[25].strip()) != float(result_item.result_item_value):
                        print (row[25]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[25], result_item.result_item_value])
                elif result_item.test_code.code == 'PLT':
                    if float(row[27].strip()) != float(result_item.result_item_value):
                        print (row[27]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[27], result_item.result_item_value])
                elif result_item.test_code.code == 'NEUT':
                    if float(row[29].strip()) != float(result_item.result_item_value):
                        print (row[29]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[29], result_item.result_item_value])
                elif result_item.test_code.code == 'LYMPH':
                    if float(row[31].strip()) != float(result_item.result_item_value):
                        print (row[31]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[31], result_item.result_item_value])
                elif result_item.test_code.code == 'MONO':
                    if float(row[33].strip()) != float(result_item.result_item_value):
                        print (row[33]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[33], result_item.result_item_value])
                elif result_item.test_code.code == 'EO':
                    if float(row[35].strip()) != float(result_item.result_item_value):
                        print (row[35]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[35], result_item.result_item_value])
                elif result_item.test_code.code == 'BASO':
                    if float(row[37].strip()) != float(result_item.result_item_value):
                        print (row[37]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[37], result_item.result_item_value])
                elif result_item.test_code.code == 'NEUT1':
                    if float(row[39].strip()) != float(result_item.result_item_value):
                        print (row[39]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[39], result_item.result_item_value])
                elif result_item.test_code.code == 'LYMPH1':
                    if float(row[41].strip()) != float(result_item.result_item_value):
                        print (row[41]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[41], result_item.result_item_value])
                elif result_item.test_code.code == 'MONO1':
                    if float(row[43].strip()) != float(result_item.result_item_value):
                        print (row[43]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[43], result_item.result_item_value])
                elif result_item.test_code.code == 'EO1':
                    if float(row[45].strip()) != float(result_item.result_item_value):
                        print (row[45]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[45], result_item.result_item_value])
                elif result_item.test_code.code == 'BASO1':
                    if float(row[47].strip()) != float(result_item.result_item_value):
                        print (row[47]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[47], result_item.result_item_value])
                else:
                    print(result_item.test_code.code)
        except ResultItem.DoesNotExist:
            if row[2] != '':
                print (row[0] + " "+ row[1]+ " " + row[2])
                error.append([row[0], row[1], row[2], 'incorrect specimen id'])
        
    
    to_file.writerows(error)  
    specimen_errors.close()
child_hematology()


import csv
from django.db import models
def child_chemistry():
    """Ensure that the all the values of the child chemistry match those in the lis."""
    file = open('child_chem.csv')
    specimen_errors = open('Child Chemistry Result Querry.csv', 'w')
    to_file = csv.writer(specimen_errors)
    lines = csv.reader(file)
    model = models.get_model('lab_result_item','ResultItem')
    error = []
    error.append(["Subject Identifier", "Event", "Specimen Identifier","Test Code", "Redcap Value", "Value on LIS"])
    spec_id = []
    
    for row in lines:
        try:
            items = model.objects.using('lab_api').filter(result__receive_identifier=row[2].strip())
            for result_item in items:
                if result_item.test_code.code == 'CL-I':
                    if row[17].strip() != float("{0:.1f}".format(result_item.result_item_value)):
                        print (row[17]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[17], result_item.result_item_value])
                elif result_item.test_code.code == 'NA-I':
                    if row[19].strip() != int(float(result_item.result_item_value)):
                        print (row[19]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[19], result_item.result_item_value])
                elif result_item.test_code.code == 'BIL-D':
                    if float(row[21].strip()) != float("{0:.1f}".format(result_item.result_item_value)):
                        print (row[21]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[21], result_item.result_item_value])
                elif result_item.test_code.code == 'CO2-L':
                    if int(float(row[23].strip())) != int(float(result_item.result_item_value)):
                        print (row[23]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[23], result_item.result_item_value])
                elif result_item.test_code.code == 'CREJ':
                    if row[25].strip() != float("{0:.1f}".format(result_item.result_item_value)):
                        print (row[25]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[25], result_item.result_item_value])
                elif result_item.test_code.code == 'GLUL':
                    if row[27].strip() != float("{0:.1f}".format(result_item.result_item_value)):
                        print (row[27]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[27], result_item.result_item_value])
                elif result_item.test_code.code == 'ALTL':
                    if row[29].strip() != float("{0:.1f}".format(result_item.result_item_value)):
                        print (row[29]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[29], result_item.result_item_value])
                elif result_item.test_code.code == 'ASTL':
                    if row[31].strip() != float("{0:.1f}".format(result_item.result_item_value)):
                        print (row[31]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[31], result_item.result_item_value])
                elif result_item.test_code.code == 'K-I':
                    if row[33].strip() != float("{0:.1f}".format(result_item.result_item_value)):
                        print (row[33]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[33], result_item.result_item_value])
                elif result_item.test_code.code == 'UREL':
                    if row[35].strip() != float("{0:.1f}".format(result_item.result_item_value)):
                        print (row[35]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[35], result_item.result_item_value])
                elif result_item.test_code.code == 'BIL-T':
                    if row[37].strip() != float("{0:.1f}".format(result_item.result_item_value)):
                        print (row[37]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[37], result_item.result_item_value])
                else:
                    print(result_item.test_code.code)
        except ResultItem.DoesNotExist:
            if row[2] != '':
                print (row[0] + " "+ row[1]+ " " + row[2])
                error.append([row[0], row[1], row[2], 'incorrect specimen id'])
        except ValueError:
            pass
    
    to_file.writerows(error)  
    specimen_errors.close()
child_chemistry()


def child_viral_load():
    """Ensure that the all the values of the child viral load match those in the lis."""
    file = open('child_viral_load_results.csv', 'r')
    specimen_errors = open('Incorrect Child Viral Load Result.csv', 'w')
    to_file = csv.writer(specimen_errors)
    lines = csv.reader(file)
    model = models.get_model('lab_result_item','ResultItem')
    error = []
    error.append(["Subject Identifier", "Event", "Specimen Identifier", "Redcap Value", "Value on LIS"])
    
    for row in lines:
        try:
            result_item = model.objects.using('lab_api').get(result__receive_identifier=row[3].strip())
            if result_item.test_code.code == 'AUVL':
                if row[19] != result_item.result_item_value:
                    print (row[19]+ " "+result_item.result_item_value)
                    error.append([row[0], row[1], row[3], row[19], result_item.result_item_value])
            else:
                print(result_item.test_code.code)
        except ResultItem.DoesNotExist:
            if row[3] != '':
                print (row[0] + " "+ row[1]+ " " + row[2])
                error.append([row[0], row[1], row[3]])
    
    to_file.writerows(error)  
    specimen_errors.close()
child_viral_load()


import csv
from django.db import models
def maternal_cd4():
    """Ensure that the all the values of the child CD4 match those in the lis."""
    file = open('maternal_cd4.csv')
    specimen_errors = open('Maternal CD4 Result Querry.csv', 'w')
    to_file = csv.writer(specimen_errors)
    lines = csv.reader(file)
    model = models.get_model('lab_result_item','ResultItem')
    error = []
    error.append(["Subject Identifier", "Event", "Specimen Identifier","Test Code", "Redcap Value", "Value on LIS"])
    spec_id = []
    
    for row in lines:
        try:
            items = model.objects.using('lab_api').filter(result__receive_identifier=row[3].strip())
            for result_item in items:
                if result_item.test_code.code == 'CD4':
                    if int(float(row[15].strip())) != int(float(result_item.result_item_value)):
                        print (row[15]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[15], result_item.result_item_value])
                elif result_item.test_code.code == 'CD4%':
                    if row[17].strip() != str(result_item.result_item_value):
                        print (row[17]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[17], result_item.result_item_value])
                elif result_item.test_code.code == 'CD8':
                    if int(float(row[21].strip())) != int(float(result_item.result_item_value)):
                        print (row[21]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[21], result_item.result_item_value])
                elif result_item.test_code.code == 'CD8%':
                    if row[19].strip() != str(result_item.result_item_value):
                        print (row[19]+ " "+result_item.result_item_value)
                        error.append([row[0], row[1], row[2], result_item.test_code.code, row[19], result_item.result_item_value])
                else:
                    print(result_item.test_code.code)
        except ResultItem.DoesNotExist:
            if row[3] != '':
                print (row[0] + " "+ row[1]+ " " + row[3])
                error.append([row[0], row[1], row[3], 'incorrect specimen id'])
    
    to_file.writerows(error)  
    specimen_errors.close()
maternal_cd4()
