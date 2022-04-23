from django import forms
from StudentApp.models import StudentDB,User_Info,Registration,Contact_Us,Notis,Event
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        g = (('Male','Male'),('Female','Female'))
        s = (('A2','A2'),('B2','B2'),('A1','A1'),('B1','B1'))
        d = (('Computer','Computer'),('Electronics','Electronics'),(' Electrical',' Electrical'),(' Power',' Power'),
             ('  Environmental','  Environmental'),(' Civil ',' Civil '),('  Mechanical ','  Mechanical '))
        e = (('1st','1st'),('2nd','2nd'),('3rd','3rd'),('4th','4th'),('5th','5th'),('6th','6th'),('7th','7th'))

        model = StudentDB
        fields = '__all__'
        widgets = {
            'Gender': forms.RadioSelect(choices=g),
            'Section': forms.Select(choices=s),
            'Department': forms.Select(choices=d),
            'Semester': forms.Select(choices=e),
        }



class UserForm(forms.ModelForm):
    c_password = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password','c_password',
                  'is_superuser','is_staff']
        widgets = {
            'password':forms.PasswordInput(),
            'first_name':forms.TextInput(attrs={'class':'text text-dark'})

        }



class User_InfoForm(forms.ModelForm):
    class Meta:
        model = User_Info
        fields = '__all__'


class Registration_Form(forms.ModelForm):

    class Meta:
        g = (('Male', 'Male'), ('Female', 'Female'))
        model = Registration
        fields = '__all__'

        widgets = {
            'Gender': forms.RadioSelect(choices=g),
            'Present_Address': forms.Textarea()
        }


class Contact_Us_form(forms.ModelForm):

    class Meta:
        model = Contact_Us
        fields = '__all__'
    widget = {
        'Description':forms.Textarea()
    }

class NotisForm(forms.ModelForm):
    class Meta:
        model = Notis
        fields = '__all__'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
