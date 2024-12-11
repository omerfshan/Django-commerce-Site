from django import forms

class formProduct(forms.Form):
    product_name = forms.CharField(max_length=255,)
    price = forms.DecimalField(max_digits=20,decimal_places=2) 
    description = forms.CharField(widget=forms.Textarea)
    slug=forms.CharField(max_length=255)


