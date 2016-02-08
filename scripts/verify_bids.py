import csv
from edc.core.identifier.classes import CheckDigit

def check_invalid_screening_bids():
    mod = CheckDigit()
    data.append([])
    data.append(['Incorrect Screening BIDS'])
    file = open('screen_bids.txt', 'r')
    subject_identifiers = file.readlines()

    for bid in subject_identifiers:
        bid = bid.strip()
        check_digit = mod.calculate(int(bid[2:4]+bid[5:9]), modulus=97)
        if str(check_digit) != bid[-2:]:
            print ("Error: {} Is not a valid BID check digit should be {}\n".format(bid, check_digit))
            data.append([bid])
            
            
def check_invalid_enrolled_bids():
    mod = CheckDigit()
    data.append([])
    data.append(['Incorrect Enrolled BIDS'])
    file = open('enroll_bids.txt', 'r')
    subject_identifiers = file.readlines()
    enrolled_bids = []
    
    registered_subject = RegisteredSubject.objects.all()
    for subject in registered_subject:
        enrolled_bids.append(subject.subject_identifier)

    for bid in subject_identifiers:
        bid = bid.strip()
        if bid not in enrolled_bids:
            print ("Error: {} is not a valid BID".format(bid))
            data.append([bid])
    

import csv
from datetime import date, datetime

screen_file = open('Invalid Screening Bids.csv', 'w')
enroll_file = open('Invalid Enrolled Bids.csv', 'w')
to_file = csv.writer(screen_file)
data = []
check_invalid_screening_bids()
to_file.writerows(data)
to_file = csv.writer(enroll_file)
data = []
check_invalid_enrolled_bids()
to_file.writerows(data)
file.close()