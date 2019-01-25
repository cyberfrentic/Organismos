from django.urls import path
from . import views

urlpatterns = [
	path('EntradasAlmacenGeneral/', views.EntradasAlmacenGeneral, name='EntradasAlmacenGeneral'),
	path('EntradasComprasDirectas/', views.EntradasComprasDirectas, name='EntradasComprasDirectas'),
]