from django.db import models

# MODELS FOR PRODUCT CATEGORY
class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
