from  django import forms
from .models import Teacher, Subject, SubjectAssignment, SubjectRegistration
from students.models import AcademicYear, Student

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['firstname', 'lastname', 'title', 'gender', 'email', 'phone_number', 'marital_status', 'date_of_birth']
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'title': 'Title',
            'gender': 'Gender',
            'email': 'Email',
            'phone_number': 'Phone',
            'marital_status': 'Marital Status',
            'date_of_birth': 'Date of Birth',

        }
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),



        }


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['subject_name']
        labels = {
            'subject_name': 'Subject Name',

        }
        widgets = {
            'subject_name': forms.TextInput(attrs={'class': 'form-control'}),

        }

class Assign_teacherForm(forms.ModelForm):
    class Meta:
        model = SubjectAssignment
        fields = ['teacher_name','subject','grade_name','academic_year']
        labels = {
            'teacher_name': 'Teacher Name',
            'subject': 'Subject Name',
            'grade_name': 'Class Name',
            'academic_year': 'Academic Year'

        }
        widgets = {}

class AcademicYearForm(forms.Form):
    academic_year = forms.ModelChoiceField(
        queryset=AcademicYear.objects.all(),
        empty_label="Select Academic Year",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class SubjectRegistrationForm(forms.ModelForm):
    class Meta:
        model = SubjectRegistration
        fields = ['stud_name', 'academic_year','grade_name', 'subject_name', 'scores']
        labels={
            'stud_name': 'Student Name'
        }

    def __init__(self, *args, **kwargs):
        # Retrieve specific arguments
        grade_name = kwargs.pop('grade_name', None)
        grade_name_value = kwargs.pop('grade_name_value', None)
        academic_year_value = kwargs.pop('academic_year_value', None)
        subject_name_value = kwargs.pop('subject_name_value', None)

        super(SubjectRegistrationForm, self).__init__(*args, **kwargs)

        # Filter stud_name queryset based on grade_name and academic_year
        if grade_name and academic_year_value:
            self.fields['stud_name'].queryset = Student.objects.filter(
                grade=grade_name,
                academic_year=academic_year_value
            )

        # Set initial values for academic_year and subject_name
        if academic_year_value:
            self.fields['academic_year'].initial = academic_year_value
            self.fields['academic_year'].widget = forms.HiddenInput()  # Hide the field
        if subject_name_value:
            self.fields['subject_name'].initial = subject_name_value
            self.fields['subject_name'].widget = forms.HiddenInput()  # Hide the field
        if grade_name_value:
            self.fields['grade_name'].initial = grade_name_value
            self.fields['grade_name'].widget = forms.HiddenInput()  # Hide the field