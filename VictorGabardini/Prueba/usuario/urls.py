from django.urls import path
from usuario import views

urlpatterns = [
	path('login/', views.login),
	path('listar/', views.listar),
	path('listar/<int:identificador>', views.perfil),
	path('crear/', views.nuevo),
]