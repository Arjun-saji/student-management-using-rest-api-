from django.contrib import admin
from .models import *

# Register your models here.



class AttendanceAdmin(admin.ModelAdmin):
	list_display = ('student', 'attendance_date', 'status')
	list_filter = ['student','attendance_date']
admin.site.register(Student)
admin.site.register(Attendance,AttendanceAdmin)