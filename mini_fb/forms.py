# mini_fb/form.py

from django import forms
from django.db import models
from django.forms import fields
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form to create a Profile project'''

    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    city = forms.CharField(label="City", required=True)
    email = forms.EmailField(label="Email", required=False)
    image = forms.URLField(label="Image")

    class Meta:
        '''inner class related to the Profile model'''

        # model to create 
        model = Profile 
        # fields related to the create profile form
        fields = ['first_name', 'last_name', 'city', 'birth_date', 'email', 'image']


class UpdateProfileForm(forms.ModelForm):
    '''A form to update a Profile project'''

    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    
    class Meta:
        model = Profile 
        fields = ['city', 'birth_date', 'email', 'image']


class CreateStatusMessageForm(forms.ModelForm):
    '''A form to create a new status message'''

    class Meta:
        model = StatusMessage
        fields = ['message']