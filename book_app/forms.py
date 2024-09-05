from django import forms 
from book_app.models import Book

class bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        
        widgets = {
            "title": forms.TextInput(attrs={'class':'form-control'}),
            "author": forms.TextInput(attrs={'class':'form-control'}),
            "descriptions": forms.TextInput(attrs={'class':'form-control'}),
            "published_date": forms.DateInput(attrs={'class':'form-control'}),
            "price": forms.TextInput(attrs={'class':'form-control'}),
            "created_at": forms.DateTimeInput(attrs={'class':'form-control'}),
            "updated_at": forms.DateTimeInput(attrs={'class':'form-control'}),

        }
        
