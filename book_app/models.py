from django.db import models
from django.core.exceptions import ValidationError

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False,blank=True, null=True) 
    updated_at=models. DateTimeField (auto_now=True,null=True, blank=True)
    
    def clean(self):
        if not self.title:
            raise ValidationError("Title must not be empty")

    # Display title in Django admin or Django shell
    # def __str__(self):
    #     return self.title

    