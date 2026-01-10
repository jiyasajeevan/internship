from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Parcel

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your username'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your email'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your phone number'})
        self.fields['address'].widget.attrs.update({'class': 'form-control', 'rows': 3, 'placeholder': 'Enter your address'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm your password'})

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'address', 'password1', 'password2')

class ParcelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sender_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Sender full name'})
        self.fields['sender_address'].widget.attrs.update({'class': 'form-control', 'rows': 3, 'placeholder': 'Sender address'})
        self.fields['receiver_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Receiver full name'})
        self.fields['receiver_address'].widget.attrs.update({'class': 'form-control', 'rows': 3, 'placeholder': 'Receiver address'})
        self.fields['receiver_phone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Receiver phone number'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 3, 'placeholder': 'Parcel description'})
        self.fields['weight'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Weight in kg'})

    class Meta:
        model = Parcel
        fields = ['sender_name', 'sender_address', 'receiver_name', 'receiver_address', 'receiver_phone', 'description', 'weight']