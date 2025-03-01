from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'
        widgets = {
            'whypay': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select'}),
            'paying_from': forms.Select(attrs={'class': 'form-control', 'onchange': 'toggleFormSections()'}),
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'pan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'PAN No'}),
            'aadhar': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aadhar No'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': 2}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name'}),
            'company_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Phone Number'}),
            'company_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Company Address', 'rows': 2}),
            'company_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Company Email'}),
            'company_pan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company PAN Number'}),
            'contact_person_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Person Name'}),
            'contact_person_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Person Number'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Donation Amount', 'min': 100, 'max': 9000000000}),
        }
        labels = {
            'whypay': 'Select', 
            'paying_from': 'Pay From'
        }