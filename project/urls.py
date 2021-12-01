# project/urls.py

from django.urls import path

from .views import *# our view class definition 

urlpatterns = [
    # map the URL to the view
    path('parts/', ShowAllPartsView.as_view(), name='show_all_parts'),
    path('employees/', ShowAllEmpsView.as_view(), name='show_all_emps'),
    path('employees/<int:pk>', ShowEmpInfoView.as_view(), name='emps_info'),
    path('parts/<int:pk>', ShowPartInfoView.as_view(), name='parts_info'),
    path('record/', ShowRecordsView.as_view(), name='show_record'),
    path('add_new_part', AddNewPartView.as_view(), name = "add_new_part"),
    path('add_new_emp', AddNewEmpView.as_view(), name = "add_new_emp"),
    
]