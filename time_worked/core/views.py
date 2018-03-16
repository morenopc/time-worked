from django.views.generic import ListView
from core.models import Employee

class TimeWorkedList(ListView):
    model = Employee
