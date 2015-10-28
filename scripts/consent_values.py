def update_infant():
    """Update registered subject fields for infants i.e. first name,  """
    infants = RegisteredSubject.objects.filter(subject_type='infant')
    count = 0
    
    for infant in infants:
        try:
            birth = InfantBirth.objects.get(registered_subject_id=infant.id)
            infant.first_name = birth.first_name
            infant.user_modified = 'fchilisa'
            infant.save()
            count += 1
            print(infant)
        except InfantBirth.DoesNotExist:
            print ('{} infant birth does not exist'.format(infant))
    print (count)
update_infant()
        
    
def update_maternal():
    """Update the is_dob_estimated field in maternal consent and regietered subject"""
    consents = MaternalConsent.objects.all()
    count = 0
    
    for subject in consents:
        subject.is_dob_estimated = '-'
        subject.user_modified = 'fchilisa'
        subject.save()
        
        try:
            rs = RegisteredSubject.objects.get(id=subject.registered_subject_id)
            rs.is_dob_estimated = '-'
            rs.user_modified = 'fchilisa'
            rs.save()
            count += 1
            print subject
        except RegisteredSubject.DoesNotExist:
            print ('{} RegisteredSubject does not exist.'.format(subject))
    print count
    
update_maternal()
