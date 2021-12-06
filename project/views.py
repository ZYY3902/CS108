from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
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

class SearchView(ListView):

    model = Part
    template_name = "project/search.html"
    context_object_name = "search"

    def get_queryset(self):

        if 'search_text' in self.request.GET:
            search_text = self.request.GET['search_text']
        
            return Part.objects.filter(part_name__contains=search_text)
    
        #default: no query provided
        return None



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

        form = CreateCheckoutPartForm()
        context['create_checkout_form'] = form

        # return this context dictionary
        return context


class AddNewPartView(CreateView):

    model = Part
    form_class = AddNewPartForm
    template_name = 'project/add_new_part.html'

class AddNewEmpView(CreateView):

    model = Employee
    form_class = AddNewEmpForm
    template_name = 'project/add_new_emp.html'


class UpdatePartInfoView(UpdateView):

    model = Part
    form_class = UpdatePartInfoForm
    template_name = 'project/update_this_part.html'


class DeletePartView(DeleteView):

    template_name = "project/delete_part.html"
    queryset = Part.objects.all()

    def get_success_url(self):
        '''Return a the URL to which we should be directed after the delete.'''

        # reverse to show the person page
        return reverse('show_all_parts')
    


def checkout_part(request, pk):
    
    if request.method == 'POST':

        form = CreateCheckoutPartForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            records = form.save(commit=False)

            part = Part.objects.get(pk=pk)

            records.automative_part = part

            records.save()
        
        else:
            print("Error!")

    url = reverse('parts_info', kwargs={'pk': pk})
    return redirect(url)



