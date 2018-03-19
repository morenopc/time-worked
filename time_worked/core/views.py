import datetime
from django.views.generic import TemplateView
from django.utils.dateparse import parse_date
from core.models import Employee, Project, TimeWorked


class TimeWorkedView(TemplateView):

    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    template_name = 'worked_time_table.html'
    queryset = None
    employees = None

    def get(self, request, *args, **kwargs):

        date = request.GET.get('d')
        if date is not None:
            datetime_date = parse_date(date)
            if datetime_date is not None:
                # Set table date
                self.yesterday = datetime_date

        self.set_queryset()
        self.set_employees()

        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def set_queryset(self):
        self.queryset = TimeWorked.objects.filter(date=self.yesterday)

    def set_employees(self):
        self.employees = self.queryset.values_list(
            'employee',
            'employee__user__first_name',
            'employee__user__last_name').distinct()

    def _get_worked_time(self):

        table = []
        rows = []
        projects = self.queryset.values_list(
            'project', 'project__name').distinct()

        for project in projects:
            rows.append(project[1])  # project name

            for employee in self.employees:
                try:
                    worked = self.queryset.get(
                        project=project[0], 
                        employee=employee[0])
                    rows.append(worked.time)
                except Exception as e:
                    rows.append(None)

            table.append(rows)
            rows = []

        return table

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['yesterday'] = self.yesterday
        context['worked_time_table'] = self._get_worked_time()
        context['employees'] = self.employees  # employee names

        return context
