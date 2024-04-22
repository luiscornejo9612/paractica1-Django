from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers,  name='teachers'),
    path('infoAlumnat/<int:student_id>/', views.infoAlumnat, name='students')
]