from django.contrib import admin

# Register your models here.
from .models import AttendanceModel,AddEmployee

admin.site.register(AttendanceModel)
admin.site.register(AddEmployee)
