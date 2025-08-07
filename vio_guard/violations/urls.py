from django.urls import path
from . import views
from django.urls import include
from .views import recent_scans

urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.getViolations, name='list_violations'),
    path('student-info/<int:student_id>/', views.getStudentDetails, name='get_student_info'),
    path('student-info/<int:student_id>/add-violation/', views.addViolation),
    path('student-info/<int:student_id>/update-violation/', views.updateViolation),
    path('user-details/', views.getUserDetails, name='get_user_details'),
    path('add-user/', views.addUser, name= 'add_user'),
    path('saso_dashboard/', views.saso_dashboard),
    path('guard_dashboard/', views.guard_dashboard),
    path('recent_scans', views.recent_scans),
    path('api-auth/', include('rest_framework.urls'))
]

