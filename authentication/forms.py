from cProfile import label
from django.contrib.auth.models import User
from django import  forms
from django.contrib.auth.forms import UserCreationForm
from .models import Lead

class SignUpForm(UserCreationForm):
    password2 =forms.CharField(label ='Confirm Password',widget=forms.PasswordInput())
    phone_number = forms.CharField(label ='Phone Number',widget=forms.NumberInput())
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}
        
class LeadRegistration(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name','email','password','status','assigned_to']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'assigned_to':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }