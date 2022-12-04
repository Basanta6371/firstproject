from django.db import models


class Employee(models.model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=30)

