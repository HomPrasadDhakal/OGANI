from accounts.forms import *
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# VIEWS FOR ADMIN PANNEL
def AdminLoginView(request):
    template = "admin/login.html"
    return render(request, template)


def AdminLoginProcess(request):
    email=request.POST.get("email")
    password=request.POST.get("password")
    user=authenticate(request=request,email=email,password=password)
    if user is not None and user.is_superuser:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("admin-dashboard"))
    else:
        messages.error(request,"Error in Login! Invalid Login Details!")
        return HttpResponseRedirect(reverse("loginpage"))


def AdminLogoutProcress(request):
    logout(request)
    messages.success(request,"successfully logout! please login again")
    return HttpResponseRedirect(reverse("loginpage"))




#VIEWS FOR COSTOMER LOGIN
def CustomerLoginProcress(request):
    email=request.POST.get("email")
    password=request.POST.get("password")
    user=authenticate(request=request,email=email,password=password)
    if user is not None and user.is_customer:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("front-end-index"))
    else:
        messages.error(request,"Error in Login! Invalid Login Details!")
        return HttpResponseRedirect(reverse("front-end-index"))


#VIEWS FOR COSTOMER REGISTRATION
def CustomerRegistrationView(request):
    form = CustomerRegistrationform()
    if request.method == "POST":
        form = CustomerRegistrationform(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_superuser = False
            user.is_staff = False
            user.is_customer = True
            user.save()
            messages.success(request,"congratulation you have successfully created your account !!!")
            return redirect("front-end-index")
        else:
            context = {'form':form}
            messages.error(request,"invalid details please try again !!!")
            return render(request,"site/index.html", context)
    context = {'form':form}
    return render(request,"site/index.html", context)

#VIEWS FOR CUSTOMER LOGOUT IN SITE
def CustomerLogoutProcess(request):
    logout(request)
    messages.success(request,"successfully logout")
    return redirect('front-end-index')