# core/urls.py
from django.urls import path
from .views import home, patient_dashboard, doctor_dashboard, administration_dashboard

urlpatterns = [
    path('', home, name='home'),
    path('patient-dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor-dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('administration-dashboard/', administration_dashboard, name='administration_dashboard'),
]

from .views import register_patient, book_appointment, medical_history ,billing_view, health_resources, patient_list
from . import views
from django.contrib import admin


urlpatterns += [
    path('admin/', admin.site.urls),  # This is the default admin URL
    path('register/', register_patient, name='register_patient'),
    path('register_doctor/', views.register_doctor, name='register_doctor'),  # New doctor registration
    path('billing/', views.billing_view, name='billing'),
    path('billing/add/', views.add_billing, name='add_billing'),
    path('billings/', views.billing_details, name='billing_details'),
    path('patients/', views.patient_list, name='patient_list'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('appointments/<int:appointment_id>/', views.appointment_details, name='appointment_details'),
    path('appointments/', views.appointment_list, name='appointment_list'),  # New URL for appointment list
    path('medical-history/', views.medical_history, name='medical_history'),
    path('add-medical-history/', views.add_medical_history, name='add_medical_history'),
    path('add-health-resource/', views.add_health_resource, name='add_health_resource'),
    path('health-resources/', views.health_resources, name='health_resources'),
    path('patients/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('patient-management/', views.patient_management, name='patient_management'),
    path('appointment-schedule/', views.appointment_schedule_view, name='appointment_schedule'),
    path('prescribing/', views.e_prescribing, name='e_prescribing'),
    path('user-management/', views.user_management, name='user_management'),
    path('users/edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('facility-management/', views.facility_management, name='facility_management'),
    path('facilities/add/', views.add_facility, name='add_facility'),
    path('appointments/', views.appointment_management, name='appointment_management'),
    path('appointments/add/', views.add_appointment, name='add_appointment'),

]
