from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# VIEWS FOR ADMIN PANNEL
@login_required(login_url="loginpage")
def AdminDashBoardView(request):
    template="admin/index.html"
    context = {}
    return render(request, template, context)


#VIEWS FOR OGANIC STORE SITE
def FrontEndView(request):
    template = "site/index.html"
    context = {}
    return render(request, template, context)