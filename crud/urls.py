from django.urls import path
from .views import home, create, update, delete

urlpatterns = [
	path('novo/', create, name='novo_produto'),
	path('editar/<int:pk>', update, name='editar_produto'),
	path('excluir/<int:pk>', delete, name='excluir_produto'),
	path('lista/', home, name='lista_produto'),
]