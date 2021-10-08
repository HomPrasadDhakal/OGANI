from django import forms
from products. models import *



#FROMS FOR PRODUCT CATEOGRY
class Product_category_from(forms.ModelForm):

    class Meta:
        model = ProductCategory
        fields = ["title",]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder':'Enter product Category',
                'class':'form-control',
            }),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        for instance in ProductCategory.objects.all():
            if instance.title == title:
                raise forms.ValidationError(" This category is already exist.")
        return title




#FORMS FOR PRODUCTS
class product_form(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['title', 'marked_price', 'selling_price', 'category', 'stock', 'shipping_time','weight','cover_image']