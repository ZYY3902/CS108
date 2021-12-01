from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from project.forms import *
from project.models import Employee, Part, Record

# Create your views here.
class ShowAllPartsView(ListView):
    ''' show a listing of all automotive parts '''

    model = Part
    template_name = 'project/allparts.html'
    context_object_name = 'allparts' # how to find the data in the template file

class ShowAllEmpsView(ListView):
    ''' show a listing of all employees '''

    model = Employee
    template_name = 'project/all_employees.html'
    context_object_name = 'allemp' # how to find the data in the template file

class ShowRecordsView(ListView):

    model = Record
    template_name = 'project/record.html'
    context_object_name = 'record' # how to find the data in the template file



class ShowEmpInfoView(DetailView):
    '''Display the profile of the a user'''

    model = Employee
    template_name = 'project/employee_info.html'
    context_object_name = 'employee'

    def get_context_data(self, **kwargs):
    
        context = super(ShowEmpInfoView, self).get_context_data(**kwargs)

        return context

class ShowPartInfoView(DetailView):
    '''Display the profile of the a user'''

    model = Part
    template_name = 'project/part_info.html'
    context_object_name = 'part'

    def get_context_data(self, **kwargs):
    
        context = super(ShowPartInfoView, self).get_context_data(**kwargs)

        return context



class AddNewPartView(CreateView):

    model = Part
    form_class = AddNewPartForm
    template_name = 'project/add_new_part.html'

class AddNewEmpView(CreateView):

    model = Employee
    form_class = AddNewEmpForm
    template_name = 'project/add_new_emp.html'





