
from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=255)

    def __str__(self):
        return f'Dr. {self.name}'

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=50)

class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_histories')
    diagnosis = models.TextField()
    medications = models.TextField()
    allergies = models.TextField()
    treatment_history = models.TextField()

    def __str__(self):
        return f"Medical History of {self.patient}"

class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=50)

class HealthResource(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title



class Prescription(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    medications = models.TextField()
    dosage = models.DateTimeField()
    duration = models.BooleanField(default=False)
    notes = models.TextField()


    def __str__(self):
        return f'Prescription for {self.patient.first_name} {self.patient.last_name}'

# Model for Appointment
class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f'Appointment with {self.patient} on {self.date}'


from django.db import models

class Medication(models.Model):
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    instructions = models.TextField()

    def __str__(self):
        return self.name


from django.db import models

class Prescription(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)  # Assuming you have a PatientProfile model
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)  # Assuming you have a DoctorProfile model
    medications = models.ManyToManyField(Medication, through='PrescriptionMedication')

class PrescriptionMedication(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medications = models.ForeignKey(Medication, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    instructions = models.TextField()

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('admin', 'Admin'), ('staff', 'Staff'), ('doctor', 'Doctor')])

    def __str__(self):
        return self.user.username

class Facility(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    resources = models.TextField()

    def __str__(self):
        return self.name

class AppointmentManage(models.Model):
    patient = models.CharField(max_length=255)
    doctor = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.appointment_date}"
