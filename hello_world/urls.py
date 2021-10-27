# file: hello_world/urls.py
# description:

from django.urls import path
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home')
]