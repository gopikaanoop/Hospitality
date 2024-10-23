
from django.shortcuts import render, redirect,get_object_or_404
from .models import Patient,Doctor, Appointment, MedicalHistory, Billing, HealthResource,Doctor,AppointmentManage,Facility
from .forms import PatientForm, AppointmentForm, BillingForm, MedicalHistoryForm, HealthResourceForm,FacilityForm,DoctorForm ,UserForm, UserProfileForm
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import AppointmentManageForm
from .models import Patient
from .models import Patient, Medication, Prescription
from .forms import PrescriptionForm

def home(request):
    return render(request, 'e_hospitality/home.html')

from django.shortcuts import render
from .models import Patient  # Assuming your patient model is called Patient

def patient_dashboard(request):
    return render(request, 'e_hospitality/patient_dashboard.html')




def doctor_dashboard(request):
    return render(request, 'e_hospitality/doctor_dashboard.html')


def administration_dashboard(request):
    return render(request, 'e_hospitality/administration_dashboard.html')


def home(request):
    resources = HealthResource.objects.all()
    return render(request, 'e_hospitality/home.html', {'resources': resources})



def register_doctor(request):
    # Fetch all doctors
    all_doctors = Doctor.objects.all()

    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new doctor
            # Redirect to the same page or another page after successful submission
            return redirect('register_doctor')  # Change this to a success page if needed
    else:
        form = DoctorForm()  # Initialize an empty form

    # Render the template with form and doctor list
    return render(request, 'e_hospitality/register_doctor.html', {
        'form': form,
        'all_doctors': all_doctors,  # Pass all doctors to the template
    })

def register_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            new_patient = form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
        all_patients = Patient.objects.all()

    return render(request, 'e_hospitality/register.html', {'form': form, 'all_patients': all_patients})


def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'e_hospitality/patient_list.html', {'patients': patients})




def book_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            new_appointment = form.save()
            return redirect('appointment_details', appointment_id=new_appointment.id)  # Redirect to appointment details with ID
    else:
        form = AppointmentForm()

    return render(request, 'e_hospitality/book_appointment.html', {'form': form})

def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)  # Fetch the specific appointment
    return render(request, 'e_hospitality/appointment_details.html', {'appointment': appointment})



def appointment_list(request):
    appointments = Appointment.objects.all()  # Retrieve all appointments
    return render(request, 'e_hospitality/appointment_list.html', {'appointments': appointments})




def medical_history(request):
    # Fetch all medical histories along with associated patient and doctor details
    medical_histories = MedicalHistory.objects.all()

    return render(request, 'e_hospitality/medical_history.html', {
        'medical_histories': medical_histories
    })



def add_medical_history(request):
    if request.method == "POST":
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_history')  # Redirect to the medical history view
    else:
        form = MedicalHistoryForm()

    return render(request, 'e_hospitality/add_medical_history.html', {'form': form})



def billing_view(request):
    billings = Billing.objects.all()  # Ensure you're querying the right model
    return render(request, 'e_hospitality/billing.html', {'billings': billings})




def add_billing(request):
    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new billing entry
            return redirect('billing')  # Redirect to billing list or any other page
    else:
        form = BillingForm()

    return render(request, 'e_hospitality/add_billing.html', {'form': form})





def billing_details(request):
    patient = get_object_or_404(Patient)
    billings = Billing.objects.filter(patient=patient)

    return render(request, 'e_hospitality/billing_details.html', {
        'patient': patient,
        'billings': billings
    })

def health_resources(request):
    resources = HealthResource.objects.all()
    return render(request, 'e_hospitality/health_resources.html', {'resources': resources})


def add_health_resource(request):
    if request.method == 'POST':
        form = HealthResourceForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new resource
            return redirect('health_resources')  # Redirect to the resources page
    else:
        form = HealthResourceForm()

    return render(request, 'e_hospitality/add_health_resources.html', {'form': form})




def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'patient_detail.html', {'patient': patient})



def patient_management(request):
    patients = Patient.objects.prefetch_related('medical_histories').all()

    return render(request, 'e_hospitality/patient_management.html', {'patients': patients})




def appointment_schedule_view(request):
    appointments = Appointment.objects.select_related('doctor', 'patient').all()

    context = {
        'appointments': appointments,
    }
    return render(request, 'e_hospitality/appointment_schedule.html', context)



def e_prescribing(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('e_prescribing')
    else:
        form = PrescriptionForm()
    prescriptions = Prescription.objects.all()

    patients = Patient.objects.all()
    medications = Medication.objects.all()

    context = {
        'form': form,
        'prescriptions': prescriptions,
    }

    return render(request, 'e_hospitality/e_prescribing_template.html', context)




def user_management(request):
    users = User.objects.all()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Create the user and save the profile
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])  # Hash the password
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('user_management')  # Redirect after creation

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'e_hospitality/user_management.html', {
        'users': users,
        'user_form': user_form,
        'profile_form': profile_form,
    })



def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user_form = UserForm(request.POST or None, instance=user)
    profile_form = UserProfileForm(request.POST or None, instance=user.userprofile)

    if user_form.is_valid() and profile_form.is_valid():
        user_form.save()
        profile_form.save()
        return redirect('user_management')

    return render(request, 'e_hospitality/edit_user.html', {'user_form': user_form, 'profile_form': profile_form})




def facility_management(request):
    facilities = Facility.objects.all()  # Fetch all facilities

    if request.method == 'POST':
        form = FacilityForm(request.POST)

        if form.is_valid():
            form.save()  # Save the new facility
            return redirect('facility_management')  # Redirect after creation
    else:
        form = FacilityForm()

    return render(request, 'e_hospitality/facility_management.html', {
        'facilities': facilities,
        'form': form,
    })



def add_facility(request):
    form = FacilityForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('facility_management')

    return render(request, 'e_hospitality/add_facility.html', {'form': form})





def appointment_management(request):
    appointments = AppointmentManage.objects.all()
    return render(request, 'e_hospitality/appointment_management.html', {'appointments': appointments})


def add_appointment(request):
    form = AppointmentManageForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('appointment_management')

    return render(request, 'e_hospitality/add_appointment.html', {'form': form})
