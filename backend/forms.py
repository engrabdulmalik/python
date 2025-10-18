from  django import forms
from .models import Product

class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email Address')
    address = forms.CharField(widget=forms.Textarea, label='Residential Address')
    field = forms.ChoiceField(choices=[('option1', 'Option 1'), ('option2', 'Option 2')], label='Select an Option')
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'