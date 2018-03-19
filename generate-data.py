import random
import datetime
from django.contrib.auth.models import User
from core.models import Employee, Project, TimeWorked


employees = ['Noah Smith', 'Olivia Black', 'Liam Lampros', 'Ava Campedelli']
for fullname in employees:
    first, last = fullname.split()
    employee = Employee()
    employee.user = User.objects.create_user(
        first_name=first,
        last_name=last,
        username=first.lower(),
        email='%s@mail.com' % first.lower(),
        password='&mpl0yiiS')
    employee.save()

projects = ['Project A', 'Project B', 'Project C', 'Project D', 'Project E']
employees = Employee.objects.all()
for project_name in projects:
    project = Project()
    project.name = project_name
    project.save()
    project.employees.add(*employees)

# yesterday, today and tomorrow 
worked_days = [
    datetime.date.today() - datetime.timedelta(days=1),
    datetime.date.today(),
    datetime.date.today() + datetime.timedelta(days=1)]
times = [0, 1, 2, 4, 6, 8]
for date in worked_days:
    for project in Project.objects.all():
        for employee in Employee.objects.all():
            hours = random.choice(times)
            if hours == 0:
                break
            time_worked = TimeWorked()
            time_worked.date = date
            time_worked.project = project
            time_worked.employee = employee
            time_worked.time = datetime.time(hours)
            time_worked.save()

# Exceptions
# Employee didn't work anyday
fullname = "Didn'tWork Anyday"
first, last = fullname.split()
employee = Employee()
employee.user = User.objects.create_user(
        first_name=first,
        last_name=last,
        username=first.lower(),
        email='%s@mail.com' % first.lower(),
        password='&mpl0yiiS')
employee.save()

# and it's in all projects
projects = Project.objects.all()
for project in projects:
    project.employees.add(employee)

# Employee only worked in Project C
fullname = 'Only ProjectC'
first, last = fullname.split()
employee = Employee()
employee.user = User.objects.create_user(
        first_name=first,
        last_name=last,
        username=first.lower(),
        email='%s@mail.com' % first.lower(),
        password='&mpl0yiiS')
employee.save()

# only project C
project = Project.objects.get(name='Project C')
project.employees.add(employee)

for date in worked_days:
    time_worked = TimeWorked()
    time_worked.date = date
    time_worked.project = project
    time_worked.employee = employee
    time_worked.time = datetime.time(random.choice([4, 6, 8]))
    time_worked.save()

# A project withou employees
project_name = 'Project F'
project = Project()
project.name = project_name
project.save()
