from django.db import models

# Create your models here.

class Profile(models.Model):
    '''Represent a profile of the Facebook users'''

    # data attributes:
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    profile_image = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this user'''

        return f'{self.first_name} {self.last_name} {self.city}'