# Generated by Django 4.0.4 on 2022-06-02 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VaccineApp', '0002_alter_vaccineapp_patientzip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccineapp',
            name='PatientOther',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
