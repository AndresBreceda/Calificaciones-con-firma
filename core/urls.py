from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('calificaciones/', views.grade_entry, name='grade_entry'),
    path('usuarios/', views.user_management, name='user_management'),
    path('firmar/', views.digital_signature, name='digital_signature'),
]