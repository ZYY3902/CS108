# mini_fb/form.py

from django import forms
from django.db import models
from django.forms import fields
from .models import Profile, StatusMessage

class CreateProfileForm(forms.ModelForm):
    '''A form to create a Profile project'''

    class Meta:
        '''inner class related to the Profile model'''

        # model to create 
        model = Profile 
        # fields related to the create profile form
        fields = ['first_name', 'last_name', 'city', 'email', 'image']

class UpdateProfileForm(forms.ModelForm):
    '''A form to update a Profile project'''

    class Meta:
        model = Profile 
        fields = ['city', 'email', 'image']