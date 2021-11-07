# quotes/form.py

from django import forms
from .models import Quote

class CreateQuoteFrom(forms.ModelForm):
    ''' A form to create a new Quote object'''

    class Meta:
        ''' additional data about this form'''

        model = Quote # which model to create
        fields = ['text', 'person'] # which fields to create


class UpdateQuoteFrom(forms.ModelForm):
    ''' A form to update a new Quote object'''

    class Meta:
        ''' additional data about this form'''

        model = Quote # which model to update
        fields = ['text', 'person'] # which fields to update
