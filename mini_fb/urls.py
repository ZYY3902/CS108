# mini_fb/urls.py

from django.urls import path

from .views import *# our view class definition 

urlpatterns = [
    # map the URL to the view
    path('', ShowAllProfilesView.as_view(), name='show_all_profiles'),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('create_profile', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
]