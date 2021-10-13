from django.urls import path
from .views import cadastrar_diarista, listar_diaristas, editar_diarista

urlpatterns = [
    path('cadastrar_diarista', cadastrar_diarista, name='cadastrar_diarista'),
    path('listar_diaristas', listar_diaristas, name='listar_diaristas'),
    path('editar_diarista/<int:diarista_id>', editar_diarista, name='editar_diarista'),
]