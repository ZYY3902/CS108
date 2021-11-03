from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Quote, Person
import random

# Create your views here.

class HomePageView(ListView):
    '''Show a listing of Quotes'''

    model = Quote # retrieve Quote objects from the database
    template_name = 'quotes/home.html'
    context_object_name = 'quotes' # how to find the data in the template file

class QuotePageView(DetailView):
    '''Display a single quote object'''
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

class RandomQuotePageView(DetailView):
    '''Display a single quote object'''
    model = Quote
    template_name = 'quotes/quote.html'
    context_object_name = 'quote'

    def get_object(self):
        '''Return one Quote object chosen at random.'''

        #obtain all quotes using the object manager
        quotes = Quote.objects.all()
        q = random.choice(quotes)
        return q


class PersonPageView(DetailView):
    '''Display a single Person object'''

    model = Person
    template_name = 'quotes/person.html'
    context_object_name = 'person'
