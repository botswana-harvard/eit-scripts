from edc.lab.lab_clinic_api.models import Result, ResultItem

def change_panel():
    results = Result.objects.filter(order__panel__name__icontains='chemistry')
    
    for result in results():
        result_items = ResultItems.objects.filter(result_id=result.id)
        if result_items.test_code == '':

