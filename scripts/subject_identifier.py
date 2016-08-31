
import csv
from edc.core.identifier.classes import CheckDigit
from string import ascii_uppercase

def create_specimen_identifier():
    specimen = "AAAA"
    clinician = 1
    #protocol = "074"
    protocol = "S"
    index = start
    
    for _ in range(start, end+1):
        while clinician < 10 and index :
            data.append([])
            data.append(["Specimen Identifiers for clinician {}0".format(clinician)])
            for letter in ascii_uppercase:
                for alpha in ascii_uppercase:
                    for letr in ascii_uppercase:
                        for l in ascii_uppercase:
                            spec = letter+alpha+letr+l
                            specimen_id = protocol+letter+alpha+str(clinician)+letr+l
                            specimen_id = letter+alpha+str(clinician)+letr+l
                            data.append([specimen_id])
                            print specimen_id
            clinician+=1       


def create_subject_identifier():
    """Create subject_identifier for screening EIT"""
    start = 1003
    end = 1103
    #protocol = "074"
    protocol = "S"
    clinician = 1
    number = "100000"
    
    check = CheckDigit()
    
    while clinician < 10 :
        data.append([])
        data.append(["Subject identifiers for clinician {}0".format(clinician)])
        number = str(long(number)+start)
        for _ in range(start, end+1):
            #seq = protocol+number
            seq = number
            check_digit = check.calculate(int(seq), modulus=97)
            identifier = protocol+"-"+number[:2]+"-"+number[2:]+"-"+str(check_digit)
            data.append([identifier])
            print identifier
            number = str(long(number)+1)

                
        clinician+=1
        number = str(clinician)+"00001"


import csv
from datetime import date, datetime

start = 1
end = 20

file = open('Subject Identifiers batch 11.csv', 'w')
to_file = csv.writer(file)
data = []
create_subject_identifier()
to_file.writerows(data)
file.close()

#file = open('Specimen Identifiers.csv', 'w')
#to_file = csv.writer(file)
#data = []
#create_specimen_identifier()
#to_file.writerows(data)
#file.close()
