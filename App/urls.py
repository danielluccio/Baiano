from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('register/', views.register, name='register'),  # Certifique-se de que essa view exista
    path('calendario/', views.calendario, name='calendario'),
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('calendar_events/', views.calendar_events, name='calendar_events'),
    path('registrar_uso_cigarro/', views.registrar_uso_cigarro, name='registrar_uso_cigarro'),
    path('deletar_registro/<int:id>/', views.deletar_registro, name='deletar_registro'),  # Excluir registro individual
    path('deletar_todos_registros/', views.deletar_todos_registros, name='deletar_todos_registros'),  # Excluir todos os registros
    path('confirmar_exclusao/<int:id>/', views.confirmar_exclusao, name='confirmar_exclusao'), # Página de Confirmação
]