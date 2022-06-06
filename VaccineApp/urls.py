from django.urls import re_path as url ,path
from VaccineApp import views

# from django.conf.urls.static import static
# from django.conf import settings

# from django.conf.urls import url

urlpatterns=[
    url(r'^patient$', views.VaccineAppApi),
    url(r'^patient/([0-9+])$', views.VaccineAppApi),
     path('Excel', views.save_file),
    
    # url(r'^employee/([0-9]+)$',views.employeeApi),
    #
    # url(r'^employee/savefile',views.SaveFile)
]