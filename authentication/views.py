from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def sign_up(request):
    fm = UserCreationForm()
    return render(request , 'authentication/signup.html',{'form':fm})
    
