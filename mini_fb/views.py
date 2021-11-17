from django.core.checks import messages
from django.db import models
from django.db.models.base import Model
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from mini_fb.forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from .models import Profile, StatusMessage

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

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm() 
        context['create_status_form'] = form
        # return this context dictionary
        return context


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


class DeleteStatusMessageView(DeleteView):
    '''A view to delete a status message'''

    template_name = "mini_fb/delete_status_form.html"
    queryset = StatusMessage.objects.all()

    def get_context_data(self, **kwargs):
        '''Override the get_context_data(self, **kwargs) method within the DeleteStatusMessageView'''

        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])

        context['st_msg'] = st_msg

        # return this context dictionary
        return context

    def get_object(self):
        '''return the StatusMessage object that should be deleted'''

        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']

        # find the StatusMessage object, and return it
        return StatusMessage.objects.filter(profile=profile_pk, pk=status_pk)
    
    def get_success_url(self):
        '''Return a the URL to which we should be directed after the delete.'''

        # read the URL data values into variables
        profile_pk = self.kwargs['profile_pk']
        
        url = reverse('show_profile_page', kwargs={'pk':profile_pk})
        return url

class ShowNewsFeedView(DetailView):

    model = Profile
    template_name = "mini_fb/show_news_feed.html"
    context_object_name = "profilepage"


class ShowPossibleFriendsView(DetailView):

    model = Profile
    template_name = "mini_fb/show_possible_friends.html"
    context_object_name = "profile"


def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False) # don't commit to database yet

            # find the profile that matches the `pk` in the URL
            profile = Profile.objects.get(pk=pk)

            # attach FK profile to this status message
            status_message.profile = profile

            # now commit to database
            status_message.save()
        
        else:
            print("Error: the form was not valid.")

    # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)

def add_friend(request, profile_pk, friend_pk):
    '''add a friend for the given profile'''

    user = Profile.objects.get(pk=profile_pk)
    friend = Profile.objects.get(pk=friend_pk)
    user.friends.add(friend)
    user.save()

    url = reverse('show_profile_page', kwargs={'pk': profile_pk})
    return redirect(url)