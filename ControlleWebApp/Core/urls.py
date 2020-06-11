from django.urls import path, include

from . import views

app_name = 'Core'

urlpatterns = [
    path('', views.paginaInicial, name='home'),
    path('login/', views.loginUsuario, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.painelUsuario, name='dashboard_home'),
]
