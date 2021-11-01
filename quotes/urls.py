# quotes/urls.py

from django.urls import path
from .views import HomePageView # our view class definition 

urlpatterns = [
    # map the URL to the view
    path('', HomePageView.as_view(), name='home_page'),
]