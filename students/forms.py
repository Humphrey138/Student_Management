from  django import forms
from .models import Student, AcademicYear

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'grade', 'academic_year', 'gender', 'live_with', 'date_of_birth','live_with_fullname','live_with_phone','live_with_address', 'sponsor_name','sponsor_phone']
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'grade': 'Class',
            'academic_year': "Academic Year",
            'gender': 'Gender',
            'live_with': 'Lives With',
            'date_of_birth': 'Date of Birth',
            'live_with_fullname': 'Student Parent Name',
            'live_with_phone': 'Parent Phone',
            'live_with_address': 'Home Address',
            'sponsor_name' : 'Sponsor Name',
            'sponsor_phone' : 'Sponsor Phone'

        }
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'live_with_fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'live_with_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'live_with_address': forms.TextInput(attrs={'class': 'form-control'}),
            'sponsor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sponsor_phone': forms.TextInput(attrs={'class': 'form-control'}),

        }

class AcademicYearForm(forms.Form):
    academic_year = forms.ModelChoiceField(
        queryset=AcademicYear.objects.all(),
        empty_label="Select Academic Year",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
