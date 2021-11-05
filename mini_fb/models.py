from django.db import models

# Create your models here.   

class Profile(models.Model):
    '''Represent a profile of the Facebook users'''

    # data attributes:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    image = models.URLField(blank=True) # url as a string

    def __str__(self):
        '''Return a string representation of this user'''

        return f'{self.first_name} {self.last_name} {self.city}'

    def get_status_messages(self):
        '''obtain status messages for the choosen Profile'''

        return StatusMessage.objects.filter(profile=self)
        

class StatusMessage(models.Model):
    '''model the data attributes of Facebook status message'''

    timestamp = models.TextField(blank=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile} {self.timestamp} {self.message}'