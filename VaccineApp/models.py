from django.db import models

# Create your models here.

class VaccineApp(models.Model):
    PatientId = models.AutoField(primary_key=True)
    PatientFirstName = models.CharField(blank=False, max_length=500)
    PatientLastName = models.CharField(blank=False, max_length=500)
    PatientDateOfBirth = models.DateField(blank=False)
    PatientAdress = models.CharField(blank=False, max_length=500)
    PatientCity = models.CharField(blank=False, max_length=500)
    PatientZip = models.IntegerField(blank=False)
    PatientLand = models.CharField(blank=False, max_length=500)
    PatientCell = models.CharField(blank=False, max_length=50)
    PatientInfected = models.BooleanField(blank=False)
    PatientDiabetes = models.BooleanField(blank=False)
    PatientCardio = models.BooleanField(blank=False)
    PatientAllergies = models.BooleanField(blank=False)
    PatientOther = models.CharField(blank=True, max_length=500)