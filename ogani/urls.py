from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from products import views as pro
from accounts import views as acc

urlpatterns = [
    path('admin/', admin.site.urls),
    #CUSTOM URLS
    #URLS FOR ADMIN PANNEL
    path('dashboard/', pro.AdminDashBoardView, name="admin-dashboard" ),
    path('admin/', acc.AdminLoginView, name="loginpage" ),
    path('admin_login_process/', acc.AdminLoginProcess, name="admin-login-process" ),
    path('admin_logout_process/', acc.AdminLogoutProcress, name="admin-logout-process" ),
    
    #URLS FOR ADMINPANNEL PASSWORD CHANGE
    path('admin_pannel_password_change/', acc.AdminPasswordChangeView, name="admin-password-change"),
    
    #URLS FOR PRODUCT CATEGORY
    path('add_product_category/', pro.Add_Product_category, name="add-product-category"),
    path('product_category_list/', pro.Product_category_list, name="product-category-list"),
    path('product_category_update/<str:pk>', pro.product_category_update, name="product-category-update"),
    path('product_category_delete/<str:pk>', pro.delete_product_category, name="product-category-delete"),
    
    #URLS FOR PRODUCTS
    path('add_procucts/', pro.Add_product, name="add-product"),
    path('update_procucts/<str:pk>', pro.Update_product, name="update-product"),
    path('procucts_list/', pro.Product_List, name="productlist"),
    path('procucts_detail/<str:pk>', pro.Product_details, name="productdetails"),
    path('procucts_delete/<str:pk>', pro.deleteProduct, name="deleteproducts"),
    
    #URLS FOR BLOGS CATEGORY
    path('add__category_blogs/', pro.Add_Blog_category, name="add-blogs-category"),
    path('blogs_category_list/', pro.Blogscategorylist, name="blogs-category-list"),
    path('blogs_category_delete/<str:pk>', pro.deleteProduct, name="blogs-category-delete"),
    path('blogs_category_update/<str:pk>', pro.blog_category_update, name="blogs-category-update"),

    #URLS FOR BLOGS
    path("add_blogs", pro.Add_blogs, name="add-blogs"),
    path("blogs_list", pro.BlogListView, name="admin-blogs-list"),
    path("delete_bogs/<str:pk>", pro.DeleteBlogs, name="delete-blogs"),
    
    #URLS FOR SITE FRONTEND
    path('', pro.FrontEndView, name="front-end-index"),
    path('costomer_login_process/', acc.CustomerLoginProcress, name="costomer-login-process"),
    path('costomer_registration_process/', acc.CustomerRegistrationView, name="costomer-registration-process"),
    path('costomer_logout_process/', acc.CustomerLogoutProcess, name="costomer-logout-process"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


