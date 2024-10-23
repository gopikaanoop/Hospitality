# core/forms.py
from django import forms
from .models import Patient, Appointment, Billing, Prescription,Doctor

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'specialty']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'age' , 'phone', 'address']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient', 'date', 'status']

class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields = ['patient', 'amount_due', 'payment_status']


# core/forms.py
from django import forms
from .models import MedicalHistory, Patient


class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ['patient', 'diagnosis', 'medications', 'allergies', 'treatment_history']


# core/forms.py
from django import forms
from .models import HealthResource

class HealthResourceForm(forms.ModelForm):
    class Meta:
        model = HealthResource
        fields = ['title', 'content']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'patient', 'date', 'status']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'reason_for_visit': forms.Textarea(attrs={'rows': 2}),
        }

from django import forms
from .models import Prescription, Medication, PrescriptionMedication

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'doctor', 'medications']

class PrescriptionMedicationForm(forms.ModelForm):
    class Meta:
        model = PrescriptionMedication
        fields = ['medications', 'dosage', 'instructions']

from django import forms
from .models import Medication

class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields = ['name',  'dosage', 'instructions']

from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['role']  # Include any other fields you have in UserProfile


from django import forms
from .models import Facility

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = ['name', 'location', 'department', 'resources']

from django import forms
from .models import AppointmentManage

class AppointmentManageForm(forms.ModelForm):
    class Meta:
        model = AppointmentManage
        fields = ['patient', 'doctor', 'department', 'appointment_date', 'appointment_time']
