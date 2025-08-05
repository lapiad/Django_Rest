from django.contrib import admin
from django.utils import timezone
from datetime import timedelta
from .models import StudentInfo, Violation, ViolationType
from .models import ViolationLogs
# adminDashboard

class ViolationAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'violation_type']
    list_filter = ['status']
    actions = ['create_new_violation_report', 'generate_weekly_report', 'view_pending_reports']

    def mark_as_pending(self, request, queryset):
        queryset.update(status='pending')
        self.message_user(request, f"{queryset.count()} reports marked as pending.")

    mark_as_pending.short_description = "Mark as Pending"

    def generate_weekly_report(self, request, queryset):
        one_week_ago = timezone.now() - timedelta(days=7)
        recent = queryset.filter(created_at__gte=one_week_ago)
        self.message_user(request, f"{recent.count()} violations reported this week.")

    generate_weekly_report.short_description = "Generate Weekly Report"

admin.site.register(Violation, ViolationAdmin)
admin.site.register(StudentInfo)
admin.site.register(ViolationType)

# adminViolationLogs

class ViolationLogsAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'violation_type', 'date_reported', 'reported_by', 'status', ]
    def student_name(self, obj):
        return obj.student.name 
    reported_by = ['user_name', 'timestamp']
    search_fields = ['violation', 'student_name', 'action']

admin.site.register(ViolationLogs, ViolationLogsAdmin)

#SummaryReportsAdmin

class SummaryReportsAdmin(admin.ModelAdmin):
    actions = ['Total Cases', 'Under Review', 'Scheduled', 'Pending']
#notdone

#reffered to council
class RefferedToCouncilAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'Violation_type', ]
    fields = ['view details', 'documents', ]

#addnewuser
class AddNewUserAdmin(admin.ModelAdmin):
    list
#notdone