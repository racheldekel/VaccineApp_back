from rest_framework import serializers
from VaccineApp.models import VaccineApp

class VaccineAppSerializer(serializers.ModelSerializer):
    class Meta:
        model=VaccineApp 
        fields=('PatientId','PatientFirstName','PatientLastName','PatientDateOfBirth','PatientAdress','PatientCity','PatientZip',
        'PatientLand','PatientCell','PatientInfected','PatientDiabetes','PatientCardio','PatientAllergies','PatientOther')

