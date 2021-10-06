from products.froms import *
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required



# VIEWS FOR ADMIN PANNEL
@login_required(login_url="loginpage")
def AdminDashBoardView(request):
    template="admin/index.html"
    context = {}
    return render(request, template, context)

#VIEWS FOR PRODUCT CATEGORY
@login_required(login_url="loginpage")
def Add_Product_category(request):
    form = Product_category_from()
    if request.method == "POST":
        form = Product_category_from(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"successfully added product category")
            return redirect('product-category-list')
    else:
        form = Product_category_from()
    template = "admin/productcategory/addproductcategory.html"
    context = {"form":form}
    return render(request, template, context)

@login_required(login_url="loginpage")
def Product_category_list(request):
    procat = ProductCategory.objects.all().order_by("-id")
    context = {"procat":procat}
    template = "admin/productcategory/productcategorylist.html"
    return render(request, template, context)

@login_required(login_url="loginpage")
def product_category_update(request, pk):
    procat = ProductCategory.objects.get(id=pk)
    form = Product_category_from(request.POST, instance=procat)
    if request.method == "POST":
        form = Product_category_from(request.POST, instance=procat)
        if form.is_valid():
            form.save()
            messages.success(request, "update product category successfully !")
            return redirect('product-category-list')
        else:
            form = Product_category_from(instance=procat)
    else:
        form = Product_category_from(instance=procat)
    template = "admin/productcategory/updateproductcategory.html"
    context = {"form":form}
    return render(request, template, context)


@login_required(login_url="loginpage")
def delete_product_category(request, pk):
    procat = ProductCategory.objects.get(id=pk)
    procat.delete()
    messages.success(request, "product category has been deleted !!!")
    return redirect('product-category-list')

#VIEWS FOR OGANIC STORE SITE
def FrontEndView(request):
    template = "site/index.html"
    context = {}
    return render(request, template, context)


