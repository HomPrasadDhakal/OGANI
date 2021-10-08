from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import user

# MODELS FOR PRODUCT CATEGORY
class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# MODELS FOR PRODUCT AND IT'S SEO SECTION
class Product(models.Model):
    title = models.CharField(max_length=255)
    marked_price = models.IntegerField()
    selling_price = models.IntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = RichTextField()
    stock = models.CharField(max_length=255)
    shipping_time = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    cover_image = models.FileField(upload_to="products/cover~_image")

    def __str__(self):
        return self.title
    

class ProductGallary(models.Model):
    image_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(upload_to="products/images", null=True, blank=True)

    def __str__(self):
        return self.packages.title


class ProductSeoSection(models.Model):
    seo_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seo_tite = models.CharField(max_length=500)
    seo_description = models.TextField()
    seo_keywords = models.CharField(max_length=500)

    def __str__(self):
        return self.seo_title
    

#MODELS FOR BLOGS AND IT'S CATEGORY AND SEO SECTION
class BlogsCategory(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

     
    def __str__(self):
        return self.title
    


class Blogs(models.Model):
    category = models.ForeignKey(BlogsCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    image = models.FileField(upload_to="blogs_pics")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

     
    def __str__(self):
        return self.title


class BlogsSeoSection(models.Model):
    bog = models.ForeignKey(BlogsCategory, on_delete=models.CASCADE)
    seo_title = models.CharField(max_length=255)
    seo_desccription = models.TextField()
    seo_keywords = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.title