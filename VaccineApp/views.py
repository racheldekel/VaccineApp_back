import xlwt

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from VaccineApp.models import VaccineApp
from VaccineApp.serializers import VaccineAppSerializer

from django.core.files.storage import default_storage
# Create your views here.
@csrf_exempt
def VaccineAppApi(request,id=0):
    if request.method=='GET':
        vaccineApp = VaccineApp.objects.all()
        vaccine_serializer=VaccineAppSerializer(vaccineApp,many=True)
        return JsonResponse(vaccine_serializer.data, safe=False)
    elif request.method=='POST':
        vaccine_data=JSONParser().parse(request)
        vaccine_serializer=VaccineAppSerializer(data=vaccine_data)
        if vaccine_serializer.is_valid():
            vaccine_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        else:
            print(vaccine_serializer.errors)
        return JsonResponse("Failed to Add",safe=False)

@csrf_exempt
def save_file(request):
    human = VaccineApp.objects.all()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Summary.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Summary')
    row_num = 0

    cols = ['PatientFirstName', 'PatientLastName', 'PatientDateOfBirth', 'PatientAdress', 'PatientCity', 'PatientZip', 'PatientLand', 'PatientCell',
            'PatientInfected', 'PatientDiabetes', 'PatientCardio', 'PatientAllergies' , 'PatientOther']

    for col_num in range(len(cols)):
        ws.write(row_num, col_num, cols[col_num])

    rows = human.values_list('PatientFirstName', 'PatientLastName', 'PatientDateOfBirth', 'PatientAdress', 'PatientCity', 'PatientZip', 'PatientLand',
                             'PatientCell', 'PatientInfected', 'PatientDiabetes', 'PatientCardio', 'PatientAllergies', 'PatientOther')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]))

    wb.save(response)
    return response