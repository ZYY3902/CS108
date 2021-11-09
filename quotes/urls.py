# quotes/urls.py

from django.urls import path

from quotes.form import CreateQuoteFrom, UpdateQuoteFrom
from .views import * # our view class definition 

urlpatterns = [
    # map the URL to the view
    path('all', HomePageView.as_view(), name='all_quotes'), 
    path('quote/<int:pk>', QuotePageView.as_view(), name='quote'),
    path('random', RandomQuotePageView.as_view(), name='random'),  # show one quote at random
    path('person/<int:pk>', PersonPageView.as_view(), name="person"), ## NEW URL TO SHOW PERSON PAGE
    path('create_quote', CreateQuoteView.as_view(), name="create_quote"), ## NEW URL TO SHOW CREATE QUOTE PAGE
    path('quote/<int:pk>/update', UpdateQuoteView.as_view(), name='update_quote'),
    path('quote/<int:pk>/delete', DeleteQuoteView.as_view(), name="delete_quote"), # URL TO SHOW THE DELETE QUOTE PAGE
]