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
    seo_tite = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter your SEO title here'
        }
    ))
    seo_description = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Enter your SEO description here'
        }
    ))
    seo_keywords = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter your SEO keywords here'
        }
    ))
    product_image = forms.FileField(required=True, widget=forms.ClearableFileInput(
        attrs={
            'class':'form-control',
            'multiple':'True',
        }
    ))
    class Meta:
        model = Product
        fields = ['title', 'marked_price', 'selling_price','description', 'category', 'stock', 'shipping_time','weight','cover_image']

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder':'Enter product title',
                'class':'form-control',
            }),
            'marked_price': forms.NumberInput(attrs={
                'placeholder':'Enter marked Price',
                'class':'form-control',
            }),
            'selling_price': forms.NumberInput(attrs={
                'placeholder':'Enter Selling Price',
                'class':'form-control',
            }),
            'description': forms.Textarea(attrs={
                'placeholder':'Enter Product description',
                'class':'form-control',
            }),
            'category': forms.Select(attrs={
                'placeholder':'Enter Product description',
                'class':'form-control',
            }),
            'stock': forms.TextInput(attrs={
                'placeholder':'Enter stock avalible',
                'class':'form-control',
            }),
            'shipping_time': forms.TextInput(attrs={
                'placeholder':'Enter Shipping time',
                'class':'form-control',
            }),
            'weight': forms.TextInput(attrs={
                'placeholder':'Enter weight/pics',
                'class':'form-control',
            }),
            'cover_image': forms.ClearableFileInput(attrs={
                'class':'form-control',
            }),
        }


#FORMS FOR BLOGS CATEGORY
class blogs_Category_form(forms.ModelForm):
    class Meta:
        model = BlogsCategory
        fields = ["title", ]

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder':'Enter product title',
                'class':'form-control',
            }),
        }