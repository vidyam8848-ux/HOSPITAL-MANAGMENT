from django import forms
from .models import booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['p_name', 'p_email', 'p_phone', 'doc_name', 'booked_on']
        
        labels = {
            'p_name': 'Patient Name',
            'P_email': 'Patient Email',
            'p_phone': 'Patient Phone',
            'doc_name': 'Doctor Name',
            'booked_on': 'Booking Date',
        }     
        
        widgets = {
            'booked_on': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'p_name': forms.TextInput(attrs={'placeholder':'Enter full name','class': 'form-control'}),
            'p_phone': forms.TextInput(attrs={'placeholder':'10-digit number','class': 'form-control'}),
            'p_email': forms.EmailInput(attrs={'placeholder':'example@gmail.com','class': 'form-control'}),
            'doc_name': forms.Select(attrs={'class': 'form-control'}),
            
        }