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

#VIEWS FOR PRODUCTS
@login_required(login_url="loginpage")
def Add_product(request):
    form = product_form()
    if request.method == "POST":
        form = product_form(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            image  = request.FILES.getlist("product_image")
            title = request.POST.get("seo_tite")
            description = request.POST.get("seo_description")
            keywords = request.POST.get("seo_keywords")
            for i in image:
                ProductGallary.objects.create(image_product=product, image=i)
            ProductSeoSection.objects.create(seo_product=product, seo_tite=title, seo_description=description, seo_keywords=keywords)
            messages.success(request,"successfully added products.")
            return redirect('productlist')
    else:
        form = product_form()

    context = {'form':form }
    template = "admin/products/addproducts.html"
    return render(request, template, context)

@login_required(login_url="loginpage")
def Update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = product_form(instance=product)
    if request.method == "POST":
        form = product_form(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save()
            image  = request.FILES.getlist("product_image")
            title = request.POST.get("seo_tite")
            description = request.POST.get("seo_description")
            keywords = request.POST.get("seo_keywords")
            for i in image:
                ProductGallary.objects.update(image_product=product, image=i)
            ProductSeoSection.objects.update(seo_product=product, seo_tite=title, seo_description=description, seo_keywords=keywords)
            messages.success(request,"successfully Updated products.")
            return redirect('productlist')
    else:
        form = product_form(instance=product)

    context = {'form':form }
    template = "admin/products/updateproduct.html"
    return render(request, template, context)


@login_required(login_url="loginpage")
def Product_List(request):
    prolist = Product.objects.all()
    context = {"prolist":prolist}
    template = "admin/products/productlist.html"
    return render(request, template, context)

@login_required(login_url="loginpage")
def Product_details(request, pk):
    prodel = Product.objects.get(id=pk)
    context = {"prodel":prodel}
    template = "admin/products/productdetails.html"
    return render(request, template, context)


@login_required(login_url="loginpage")
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    messages.success(request, "product has been deleted !!!")
    return redirect('productlist')


#VIEWS FOR OGANIC STORE SITE
def FrontEndView(request):
    template = "site/index.html"
    context = {}
    return render(request, template, context)


