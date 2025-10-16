from django import forms
from django.contrib.auth.models import User
from . import models

# -------------------------
# Admin Signup Form
# -------------------------
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if not data.isalpha():
            raise forms.ValidationError("First name sirf alphabets hona chahiye.")
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if not data.isalpha():
            raise forms.ValidationError("Last name sirf alphabets hona chahiye.")
        return data


# -------------------------
# Doctor Forms
# -------------------------
class DoctorUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if not data.isalpha():
            raise forms.ValidationError("First name sirf alphabets hona chahiye.")
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if not data.isalpha():
            raise forms.ValidationError("Last name sirf alphabets hona chahiye.")
        return data


class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['address', 'mobile', 'department', 'status', 'profile_pic']

    def clean_mobile(self):
        data = self.cleaned_data['mobile']
        if not data.isdigit():
            raise forms.ValidationError("Mobile number sirf digits hona chahiye.")
        if len(data) != 10:
            raise forms.ValidationError("Mobile number 10 digits ka hona chahiye.")
        return data


# -------------------------
# Patient Forms
# -------------------------
class PatientUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        if not data.isalpha():
            raise forms.ValidationError("First name sirf alphabets hona chahiye.")
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        if not data.isalpha():
            raise forms.ValidationError("Last name sirf alphabets hona chahiye.")
        return data


class PatientForm(forms.ModelForm):
    assignedDoctorId = forms.ModelChoiceField(
        queryset=models.Doctor.objects.all().filter(status=True),
        empty_label="Name and Department",
        to_field_name="user_id"
    )

    class Meta:
        model = models.Patient
        fields = ['address', 'mobile', 'status', 'symptoms', 'profile_pic']

    def clean_mobile(self):
        data = self.cleaned_data['mobile']
        if not data.isdigit():
            raise forms.ValidationError("Mobile number sirf digits hona chahiye.")
        if len(data) != 10:
            raise forms.ValidationError("Mobile number 10 digits ka hona chahiye.")
        return data


# -------------------------
# Appointment Forms
# -------------------------
class AppointmentForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(
        queryset=models.Doctor.objects.all().filter(status=True),
        empty_label="Doctor Name and Department",
        to_field_name="user_id"
    )
    patientId = forms.ModelChoiceField(
        queryset=models.Patient.objects.all().filter(status=True),
        empty_label="Patient Name and Symptoms",
        to_field_name="user_id"
    )

    class Meta:
        model = models.Appointment
        fields = ['description', 'status']


class PatientAppointmentForm(forms.ModelForm):
    doctorId = forms.ModelChoiceField(
        queryset=models.Doctor.objects.all().filter(status=True),
        empty_label="Doctor Name and Department",
        to_field_name="user_id"
    )

    class Meta:
        model = models.Appointment
        fields = ['description', 'status']


# -------------------------
# Contact Form
# -------------------------
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 30})
    )

    def clean_Name(self):
        data = self.cleaned_data['Name']
        if not data.isalpha():
            raise forms.ValidationError("Name sirf alphabets hona chahiye.")
        return data
