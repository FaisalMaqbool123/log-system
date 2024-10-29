from .models import Product
from django import forms
class Productform(forms.ModelForm):
    class Meta:
        model=Product
        fields=['id','title','price','description']
    