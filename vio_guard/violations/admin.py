from django.contrib import admin
from django.contrib import admin
from .models import StudentInfo, Violation, ViolationType

# Register your models here.

class ViolationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_id', 'violation_type', 'status', 'reported_by')
    search_fields = ('student_id__name', 'violation_type__name', 'status', 'reported_by__name')
    list_filter = ('violation_type', 'status', 'reported_by')
    list_display = ('id', 'student_id', 'violation_type', 'status', 'reported_by')

admin.site.register(Violation, ViolationAdmin)
admin.site.register(StudentInfo)
admin.site.register(ViolationType)