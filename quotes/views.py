from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from quotes.form import CreateQuoteFrom, UpdateQuoteFrom
from .models import Quote, Person
from django.urls import reverse
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


class CreateQuoteView(CreateView):
    '''Create a new Quote object and store it in the database'''

    model = Quote
    form_class = CreateQuoteFrom # which form to use to create the Quote
    template_name = "quotes/create_quote_form.html" # delegate the display to this template


class UpdateQuoteView(UpdateView):
    '''Update a new Quote object and store it in the database'''

    model = Quote
    form_class = UpdateQuoteFrom # which form to use to create the Quote
    template_name = "quotes/update_quote_form.html" # delegate the display to this template


class DeleteQuoteView(DeleteView):
    '''A view to delete a quote and remove it from the database.'''

    template_name = "quotes/delete_quote.html"
    queryset = Quote.objects.all()

    def get_success_url(self):
        '''Return a the URL to which we should be directed after the delete.'''

        # get the pk for this quote
        pk = self.kwargs.get('pk')
        quote = Quote.objects.filter(pk=pk).first() # get one object from QuerySet
        
        # find the person associated with the quote
        person = quote.person

        # reverse to show the person page
        return reverse('person', kwargs={'pk':person.pk})
