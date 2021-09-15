from bedavailability.views import home, HospitalDetailView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', home, name='homepage'),
    path('hospital/<int:pk>', HospitalDetailView.as_view(), name='hospital_detail'),
]