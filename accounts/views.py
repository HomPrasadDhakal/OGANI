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
    return HttpResponseRedirect(reverse("loginpage"))