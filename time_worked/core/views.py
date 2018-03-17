import datetime
from django.views.generic import ListView
from core.models import Employee, Project

class TimeWorkedList(ListView):
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['yesterday'] = datetime.date.today() - datetime.timedelta(days=1)
        return context
