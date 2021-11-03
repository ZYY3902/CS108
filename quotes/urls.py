# quotes/urls.py

from django.urls import path
from .views import HomePageView, PersonPageView, QuotePageView, RandomQuotePageView # our view class definition 

urlpatterns = [
    # map the URL to the view
    path('all', HomePageView.as_view(), name='all_quotes'), 
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'),
    path('random', RandomQuotePageView.as_view(), name='random'),  # show one quote at random
    path('person/<int:pk>', PersonPageView.as_view(), name="person"), ## NEW URL TO SHOW PERSON PAGE
]