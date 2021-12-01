from django.db import models
from django.urls import reverse


# Create your models here.
class Part(models.Model):
    ''' information about the automotive parts '''

    # date attributes:
    part_id = models.TextField(blank=True)
    part_name = models.TextField(blank=True)
    category = models.TextField(blank=True)
    quantity = models.IntegerField(blank=False)
    manufactured_year = models.TextField(blank=True)
    image = models.URLField(blank=True)

    def __str__(self):
        
        return f'{self.part_id} - {self.category}'

    def get_absolute_url(self):

        return reverse("parts_info", kwargs={'pk': self.pk})


class Employee(models.Model):
    ''' information about the employee '''

    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=False)
    employee_id = models.TextField(blank=False)
    email = models.EmailField(blank=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):

        return reverse("emps_info", kwargs={'pk': self.pk})

    

class Record(models.Model):
    ''' show a list of records about the automotive parts '''

    automotive_parts = models.ForeignKey('Part', on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    checkout_date = models.DateField(blank=False)
    return_date = models.DateField(blank=True,null=True)
    part_condition = models.TextField(blank=True)

    def __str__(self):
        
        return f'{self.automotive_parts.part_id} - {self.employee.employee_id}'

    



