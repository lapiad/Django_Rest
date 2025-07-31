from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('login', views.login, name='login'),
    path('', views.getViolations, name='list_violations'),
    path('student-info/<int:student_id>/', views.getStudentDetails, name='get_student_info'),
    path('student-info/<int:student_id>/add-violation/', views.addViolation),
    path('student-info/<int:student_id>/update-violation/', views.updateViolation),
    path('user-details/', views.getUserDetails, name='get_user_details'),
    path('add-user/', views.addUser, name= 'add_user'),
    path('api-auth/', include('rest_framework.urls'))
]

