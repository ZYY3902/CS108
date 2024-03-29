from django.core.checks import messages
from django.db import models
from django.urls import reverse

# Create your models here.   

class Profile(models.Model):
    '''Represent a profile of the Facebook users'''

    # data attributes:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    image = models.URLField(blank=True) # url as a string
    friends = models.ManyToManyField("self")

    def __str__(self):
        '''Return a string representation of this user'''

        return f'{self.first_name} {self.last_name} {self.city}'

    def get_status_messages(self):
        '''obtain status messages for the choosen Profile'''

        return StatusMessage.objects.filter(profile=self)

    def get_absolute_url(self):
        '''Return a URL to display a profile object'''

        return reverse("show_profile_page", kwargs={'pk': self.pk})

    def get_friends(self):
        '''return all friends of selected profile'''

        return Profile.objects.filter(friends=self)
    
    def get_news_feed(self):
        '''return news feed items of the selected profile'''
        
        news = StatusMessage.objects.filter(profile__in=self.get_friends()).order_by("-timestamp")
        return news
    
    def get_friend_suggestions(self):

        friend_suggestions = Profile.objects.exclude(id=self.pk)
        
        friend = self.get_friends()
        possible_friends = friend_suggestions.exclude(pk__in=friend)
        
        return possible_friends


class StatusMessage(models.Model):
    '''model the data attributes of Facebook status message'''

    timestamp = models.TimeField(blank=True, auto_now_add=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    image =models.ImageField(blank=True)

    def __str__(self):
        return f'{self.profile} - "{self.message}"'
