from django.db import models
from django.urls import reverse
import random

# Create your models here.

class Person(models.Model):
    '''Represent a Person who said something notable'''

    name = models.TextField(blank=False)
    
    def __str__(self):
        '''Return a string representaton of this Person.'''
        return self.name
    
    def get_random_image(self):
        '''Return an image of this person, selected at random.'''

        # find all images for this person:
        images = Image.objects.filter(person=self)

        # select one at random to return
        return random.choice(images)
    
    def get_all_quotes(self):
        '''Return all quotes for this Person.'''

        # use the object manager to filter Quotes by this person's pk:
        return Quote.objects.filter(person=self)

    def get_all_images(self):
        '''Return all images for this Person.'''

        # use the object manager to filter Image by this person's pk:
        return Image.objects.filter(person=self)


class Quote(models.Model):
    '''Represent a quote by a famous person'''

    # data attributes:
    text = models.TextField(blank=True)
    person = models.ForeignKey('Person', on_delete=models.CASCADE)
    # author = models.TextField(blank=True)
    # image_url = models.URLField(blank=True)

    def __str__(self):
        '''Return a string representation of this quote'''

        return f'"{self.text}" - {self.person}'

    def get_absolute_url(self):
        '''Return a URL to display this quote object'''

        return reverse("quote", kwargs={'pk': self.pk})


class Image(models.Model):
    '''Represent an image, which is associated with a Person.'''

    image_url = models.URLField(blank=True) # url as a string
    person = models.ForeignKey('Person', on_delete=models.CASCADE)

    def __str__(self):
        '''Return a string representation of this image.'''

        return self.image_url
