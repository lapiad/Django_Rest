from django.contrib import admin
from django.utils import timezone
from datetime import timedelta
from .models import StudentInfo, Violation, ViolationType
from .models import ViolationLogs, UserManagement
from django.utils.html import format_html
from django.contrib import messages

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

#ViolationLogs
class ViolationLogAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'violation_type', 'date_reported', 'reported_by', 'status', ]
    def student_name(self, obj):
        return obj.student.name 
    reported_by = ['user_name', 'timestamp']
    search_fields = ['violation', 'student_name', 'action']

admin.site.register(ViolationLogs, ViolationLogAdmin)

#UserManagement 
class UserManagementAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'role']

admin.site.register(UserManagement, UserManagementAdmin)

#SummaryReportsAdmin
class SummaryReportsAdmin(admin.ModelAdmin):
    actions = ['mark_total_cases', 'mark_under_review', 'mark_scheduled', 'mark_pending']

    def mark_total_cases(self, request, queryset):
        updated = queryset.update(status='Total Cases')
        self.message_user(request, f"{updated} reports marked as Total Cases", messages.SUCCESS)

    def mark_under_review(self, request, queryset):
        updated = queryset.update(status='Under Review')
        self.message_user(request, f"{updated} reports marked as Under Review", messages.SUCCESS)

    def mark_scheduled(self, request, queryset):
        updated = queryset.update(status='Scheduled')
        self.message_user(request, f"{updated} reports marked as Scheduled", messages.SUCCESS)

    def mark_pending(self, request, queryset):
        updated = queryset.update(status='Pending')
        self.message_user(request, f"{updated} reports marked as Pending", messages.SUCCESS)

#referred to council
class ReferredToCouncilAdmin(admin.ModelAdmin):
    list_display = ['id', 'student_name', 'violation_type', 'view_details']
    fields = ['student_name', 'violation_type', 'documents']
    readonly_fields = ['view_details']

    def view_details(self, obj):
     return format_html('<a href="/admin/app/referredtocouncil/{}/change/">View</a>', obj.id)



