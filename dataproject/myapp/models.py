from django.db import models
from django.contrib import admin


# Create your models here.
class Employee (models.Model):
    emp_id=models.CharField(primary_key=True,max_length=4,help_text="emp_id")
    ename=models.CharField(max_length=50)
    post=models.CharField(max_length=20)
    salary=models.IntegerField()
    email=models.EmailField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('emp_id','ename','post','salary','email')