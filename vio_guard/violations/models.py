from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

class UserDetails(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45, null=True)
    last_name = models.CharField(max_length=45)
    role_id = models.IntegerField
    user_id = models.IntegerField
    position = models.CharField(max_length=45)

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    roledescription = models.CharField(max_length=45)

class StudentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=45)
    first_name = models.CharField(max_length=45)
    middle_name = models.CharField(max_length=45, null=True)
    last_name = models.CharField(max_length=45)
    birth_date = models.DateField()
    course = models.CharField(max_length=45)
    year = models.CharField(max_length=45)  
    section = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)

class Violation(models.Model):
    id = models.AutoField(primary_key=True)
    violation_type = models.CharField(max_length=45)
    student_name = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    description = models.TextField()
    reported_by = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='violations_reported')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, auto_now=True)
    status = models.CharField(max_length=45, default='Pending')
    approved_by = models.ForeignKey(UserDetails, on_delete=models.SET_NULL, null=True, blank=True, related_name='violations_approved')

class Image(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    violation_id = models.ForeignKey(Violation, on_delete=models.CASCADE, related_name='images')

class ViolationType(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=45)
    description = models.TextField()
    
    def __str__(self):
        return f"Violation by {self.student_id} on {self.date_reported}"
    

#admindashboard

class Dashboard(models.Model):
    total_violations = models.PositiveIntegerField(default=0)
    active_cases = models.PositiveIntegerField(default=0)
    student_involved = models.PositiveIntegerField(default=0)
    resolved = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Dashboard Summary: {self.total_violations} violations"

class ViolationLogs(models.Model):
    list_display = models.CharField(max_length =500)
    violation_type = models.CharField(max_length = 500)
    date_reported = models.PositiveIntegerField(default = 0)
    status = models.CharField(max_length = 45)

    def __str__(self):
        return f"Dashboard Summary: {self.total_logs} violations logs"

class UserManagement(models.Model):
    list_display = models.CharField(max_length = 45)
    emails = models.CharField(max_length = 500)
    role = models.CharField(max_length = 45)

    def __str__(self):
        return f"Dashboard Summary: {self.user_management} user management"
