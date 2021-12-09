# project/forms.py

from django import forms
from django.db import models
from django.db.models.fields import EmailField
from django.forms import fields
from django.forms.models import BaseInlineFormSet
from .models import *

class AddNewPartForm(forms.ModelForm):
    '''A form to create a new Part object'''

    part_id = forms.CharField(label="Part ID", required=True)
    part_name = forms.CharField(label="Part Name", required=True)
    category = forms.CharField(label="Category", required=True)
    quantity = forms.IntegerField(label="Quantity", required=True)
    manufactured_year = forms.CharField(label="Manufactured Year", required=True)
    image = forms.URLField(label="Image")

    class Meta:
        '''inner class related to this form'''

        # model to create 
        model = Part 
        # fields related to the create profile form
        fields = ['part_id', 'part_name', 'category', 'quantity', 'manufactured_year', 'image']



class AddNewEmpForm(forms.ModelForm):
    '''A form to create a new Employee object'''

    first_name = forms.CharField(label="First Name", required=True)
    last_name = forms.CharField(label="Last Name", required=True)
    employee_id = forms.CharField(label="Employee ID", required=True)
    email = forms.EmailField(label="Email", required=True)

    class Meta:
        '''inner class related to this form'''

        # model to create 
        model = Employee 
        # fields related to the create profile form
        fields = ['first_name', 'last_name', 'employee_id', 'email']



class CreateCheckoutPartForm(forms.ModelForm):
    '''A form to checkout a Part object'''

    checkout_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2022,2012,-1),),)
    return_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2022,2012,-1),),)

    class Meta:
        '''inner class related to this form'''

        # model to create
        model = Record
        # fields related to the create profile form
        fields = ['employee', 'automotive_parts', 'checkout_date', 'return_date']



class UpdatePartInfoForm(forms.ModelForm):
    '''A form to update a Part object'''

    class Meta:
        '''inner class related to this form'''

        # model to create
        model = Part
        # fields related to the create profile form
        fields = ['part_id', 'part_name', 'part_condition']