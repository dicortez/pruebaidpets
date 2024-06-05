from django.urls import path
from . import views



urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('Mascotas', views.Mascotas, name='Mascotas'),
    path('registrar_mascotas', views.registrar_mascotas, name='registrar_mascotas'),
    path('editar_mascotas', views.editar_mascotas, name='editar_mascotas'),
    path('signup', views.signup, name='signup'),
    path('login', views.iniciar_sesion, name='login'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar_sesion'),

]