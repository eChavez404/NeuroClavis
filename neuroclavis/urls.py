from django.urls import path
from .views import SessaoJogoAPI

urlpatterns = [
    path('sessoes/', SessaoJogoAPI.as_view(), name='registrar_sessao'),
]