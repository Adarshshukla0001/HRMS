from django.contrib import admin
from . models import Employee, Nfc,Salary,Attend
# Register your models here.
admin.site.register(Employee)
admin.site.register(Nfc)
admin.site.register(Salary)
admin.site.register(Attend)
