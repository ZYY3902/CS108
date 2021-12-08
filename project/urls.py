# project/urls.py

from django.urls import path

from .views import * # our view class definition 

urlpatterns = [
    # map the URL to the view
    path('parts/', ShowAllPartsView.as_view(), name='show_all_parts'), # URL to show all automotive parts
    path('employees/', ShowAllEmpsView.as_view(), name='show_all_emps'), # URL to show all employees
    path('employees/<int:pk>', ShowEmpInfoView.as_view(), name='emps_info'), # Show information about this employee
    path('parts/<int:pk>', ShowPartInfoView.as_view(), name='parts_info'), # Show information about this part
    path('records/', ShowRecordsView.as_view(), name='show_record'), # URL to show rental records
    path('add_new_part', AddNewPartView.as_view(), name = 'add_new_part'), # URL to show add a new part page
    path('add_new_emp', AddNewEmpView.as_view(), name = 'add_new_emp'), # URL to show add a new employee page
    path('search/', SearchView.as_view(), name='search'), # URL for searching
    path('parts/<int:pk>/checkout_form', checkout_part, name='checkout_form'), # URL to create a checkout
    path('parts/<int:pk>/update', UpdatePartInfoView.as_view(), name='update_part'), # URL to show update part info page
    path('parts/<int:pk>/delete', DeletePartView.as_view(), name="delete_part"), # URL to delete a part
]