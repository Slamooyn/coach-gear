from django.urls import path
from main.views import add_employee,show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]