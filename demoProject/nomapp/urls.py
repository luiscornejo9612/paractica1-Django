from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers,  name='teachers'),
    path('infoAlumnat/<int:student_id>/', views.infoAlumnat, name='students'),
    path('user-form/', views.user_form, name='user_form'),
    path('update-user/<str:pk>', views.update_user, name='update-user'),
    path('delete-user/<str:pk>', views.delete_user, name='delete-user'),
]