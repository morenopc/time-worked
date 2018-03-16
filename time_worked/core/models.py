from datetime import date 
from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    """Employee records"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % self.user.get_full_name()


class Project(models.Model):
    """Project records"""

    name = models.CharField(max_length=128)
    employees = models.ManyToManyField(Employee, through='TimeWorked')

    def __str__(self):
        return '%s' % self.name


class TimeWorked(models.Model):
    """Time worked by a employee in a project"""

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    time = models.TimeFiled()
