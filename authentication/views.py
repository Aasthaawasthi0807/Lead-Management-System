from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm
from django.contrib.auth import authenticate, login,logout,update_session_auth_hash
from .forms import LeadRegistration

from .models import Lead , Remark

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
                pn = fm.cleaned_data['phone_number']
                pb = fm.cleaned_data['public']
                reg = Lead(first_name = nm, email=em,assigned_to=am,status=sm,phone_number=pn,public=pb)
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


"""
#Base
def user_profile(request):
    if request.user.is_authenticated:
      return render(request , 'authentication/base.html' ,{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')"""

def user_profile(request):
    if request.user.is_authenticated:
        hot_no = Lead.objects.filter(status='Hot').count()
        hot_no = int(hot_no)
        print('Hot leads are',hot_no)

        med_no = Lead.objects.filter(status='Med').count()
        med_no = int(med_no)
        print('Med leads are',med_no)

        grey_no = Lead.objects.filter(status='Grey').count()
        grey_no = int(grey_no)
        print('Grey leads are',grey_no)

        labels= ['Hot','Grey','Med']
        data =[hot_no,med_no,grey_no]
        context = {'status_list':labels ,'number_list':data}
        return render(request,'authentication/profile.html',context)
    else:
        return HttpResponseRedirect('/login/')


