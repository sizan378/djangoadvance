from statistics import mode
from django.db import models

class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=100)
    stuemail = models.EmailField()
    stupass = models.CharField(max_length=100)


    def __str__(self):
        return self.stuname