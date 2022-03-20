from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from .forms import LeadRegistration
from .models import Lead

#Home view Function
def home(request):
    return render(request,'authentication/home.html')

# Signup View Function
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully!!')
            fm.save()
    else:        
     fm = SignUpForm()
    return render(request,"signup.html",{'form':fm})
    
#login View Function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname , password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Succesfully !!')
                    return HttpResponseRedirect('/addandshow/')
        else:
            fm = AuthenticationForm()
        return render(request,"login.html",{'form':fm})
    else:
        return HttpResponseRedirect('/addandshow/') 



#Logout View Function
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#Change Password with old Password
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data =request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request ,fm.user )
                messages.success(request, 'Password Changed Successfully!!')
                return HttpResponseRedirect('/addandshow/')
        else:   
            fm =PasswordChangeForm(user=request.user)
        return render(request,'authentication/changepass.html' , {'form':fm})
    else:
        return HttpResponseRedirect('/error/')



"""
#Base
def user_profile(request):
    if request.user.is_authenticated:
      return render(request , 'authentication/base.html' ,{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')"""

#This function will Add new Lead and Show all leads
def add_show(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = LeadRegistration(request.POST)
            if fm.is_valid():
                nm = fm.cleaned_data['first_name']
                em = fm.cleaned_data['email']
                am = fm.cleaned_data['assigned_to']
                sm = fm.cleaned_data['status']
                pw = fm.cleaned_data['password']
                reg = Lead(first_name = nm, email=em,assigned_to=am,status=sm,password=pw)
                reg.save()
                fm = LeadRegistration()
        else:
            fm = LeadRegistration()
        led = Lead.objects.all()
            


        return render(request, 'authentication/addandshow.html',{'form':fm ,'ld':led , 'name':request.user})
    else:
        return HttpResponseRedirect('/login/')



#This function will delete Leads
def delete_data(request , id):
    if request.method == 'POST':
        pi = Lead.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/addandshow/')


#This Function will Update or Edit
def update_data(request, id):
    if request.method == 'POST':
        pi = Lead.objects.get(pk=id)
        fm = LeadRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Lead.objects.get(pk=id)
        fm = LeadRegistration(instance=pi)
    return render(request, 'authentication/updatelead.html' , {'form':fm})


#Lead login function
def lead_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            fname = fm.cleaned_data['username']
            lpass = fm.cleaned_data['password']
            lead = authenticate(username=fname,password=lpass)
            if lead is not None:
                login(request,lead)
                return HttpResponseRedirect('/profile/')
    else:  
        fm = AuthenticationForm()
    return render(request,'authentication/login1.html',{'form':fm})


#Profile
def lead_profile(request):
    return render(request , 'authentication/profile.html')