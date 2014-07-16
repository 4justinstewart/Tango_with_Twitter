from django import forms
from deals.models import Company, Deal

class CompanyForm(forms.ModelForm):
    address = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(attrs={'placeholder': "Ex. 1865 N. Milwaukee Chicago IL 60647", 'autofocus': True}),
    )
    twitter_handle = forms.CharField(
        max_length=15,  
        widget=forms.TextInput(attrs={'placeholder': 'Ex. @Irazu_Chicago'})
    )

    class Meta:
        model = Company

class DealForm(forms.ModelForm):
    body = forms.CharField(max_length=140, help_text="What's the deal?  Ex. Free Oatmeal Shake")

    class Meta:
        model = Deal
        fields = ('body',)  # We do this to hide the foreign key.

