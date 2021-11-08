from random import randint
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from mini_fb.form import CreateProfileForm, UpdateProfileForm
from .models import Profile

# Create your views here.

class ShowAllProfilesView(ListView):
    '''Show a listing of user profiles'''

    model = Profile 
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'allprofiles' # how to find the data in the template file

class ShowProfilePageView(DetailView):
    '''Display the profile of the a user'''

    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'profilepage'

class CreateProfileView(CreateView):
    '''Display a create view for creating a profile'''

    model = Profile
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

class UpdateProfileView(UpdateView):
    '''Display a create view for creating a profile'''

    model = Profile
    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'

