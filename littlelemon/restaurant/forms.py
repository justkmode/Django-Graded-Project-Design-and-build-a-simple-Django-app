from django import forms

class BookingForm(forms.Form):
    # Define your form fields here
    name = forms.CharField(max_length=100)
    date = forms.DateField()
    # Add more fields as necessary
