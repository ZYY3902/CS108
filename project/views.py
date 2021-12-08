from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from project.forms import *
from project.models import Employee, Part, Record

# Create your views here.
class ShowAllPartsView(ListView):
    ''' show a listing of all automotive parts '''

    model = Part # retrieve Part objects from the database
    template_name = 'project/allparts.html' # delegate the display to this template
    context_object_name = 'allparts' # variable name used to find the data in the template file



class ShowAllEmpsView(ListView):
    ''' show a listing of all employees '''

    model = Employee # retrieve Employee objects from the database
    template_name = 'project/all_employees.html' # delegate the display to this template
    context_object_name = 'allemp' # variable name used to find the data in the template file



class ShowRecordsView(ListView):
    ''' show a listing of all records'''

    model = Record # retrieve Record objects from the database
    template_name = 'project/record.html' # delegate the display to this template
    context_object_name = 'record' # variable name used to find the data in the template file



class SearchView(ListView):
    ''' return the results of the Part searches '''

    model = Part # retrieve Part objects from the database
    template_name = "project/search.html" # delegate the display to this template
    context_object_name = "search" # variable name used in the template

    def get_queryset(self):
        ''' return a queryset of part objects that matched the searching '''

        # if find, return the name of the item searched
        if 'search_text' in self.request.GET:
            search_text = self.request.GET['search_text']
        
            return Part.objects.filter(part_name__contains=search_text)
    
        #default case: no query provided
        return None



class ShowEmpInfoView(DetailView):
    ''' display the info of this user '''

    model = Employee # retrieve Employee objects from the database
    template_name = 'project/employee_info.html' # delegate the display to this template
    context_object_name = 'employee' # variable name used in the template

    def get_context_data(self, **kwargs):
        '''Return a dictionay with context data for this template to use'''

        # get the default context data:
        # this will include the employee info for this page view
        context = super(ShowEmpInfoView, self).get_context_data(**kwargs)

        # return the context dictionary
        return context



class ShowPartInfoView(DetailView):
    ''' display the info of this part '''

    model = Part # retrieve Part objects from the database
    template_name = 'project/part_info.html' # delegate the display to this template
    context_object_name = 'part' # variable name used in the template

    def get_context_data(self, **kwargs):
        '''Return a dictionay with context data for this template to use'''

        # get the default context data:
        # this will include the part info for this page view
        context = super(ShowPartInfoView, self).get_context_data(**kwargs)

        # create a part checkout form
        form = CreateCheckoutPartForm()
        context['create_checkout_form'] = form

        # return this context dictionary
        return context



class AddNewPartView(CreateView):
    ''' a view to create a new part and store in the database '''

    model = Part # retrieve Part objects from the database
    form_class = AddNewPartForm # form used to create a new part 
    template_name = 'project/add_new_part.html' # delegate the display to this template



class AddNewEmpView(CreateView):
    ''' a view to create a new employee and store in the database '''

    model = Employee # retrieve Employee objects from the database
    form_class = AddNewEmpForm # form used to create a new employee
    template_name = 'project/add_new_emp.html' # delegate the display to this template



class UpdatePartInfoView(UpdateView):
    ''' a view to update a part object and store it in the database '''

    model = Part # retrieve Part objects from the database
    form_class = UpdatePartInfoForm # form used to update a new part's information
    template_name = 'project/update_this_part.html' # delegate the display to this template



class DeletePartView(DeleteView):
    ''' a view to delete a part and remove it from the database '''

    template_name = "project/delete_part.html" 
    queryset = Part.objects.all() 

    def get_success_url(self):
        '''Return a the URL to which we should be directed after the delete.'''

        # reverse to show the all parts page
        return reverse('show_all_parts')
    


def checkout_part(request, pk):
    ''' a custom view that handles the part checkout submission'''
    
    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # create a CreateCheckoutPart object from the request's POST data
        form = CreateCheckoutPartForm(request.POST or None, request.FILES or None)

        # check if the form is valid, save the object to database
        if form.is_valid():

            # cerate a record object with the data saved in the CreateCheckoutPartForm
            records = form.save(commit=False)

            # find the part that matches the `pk` in the URL
            part = Part.objects.get(pk=pk)

            # attach FK profile to this record
            records.automative_part = part

            # commit to the database
            records.save()
        
        else:
            print("Error!")

    # redirect the user to the part info page
    url = reverse('parts_info', kwargs={'pk': pk})
    return redirect(url)


