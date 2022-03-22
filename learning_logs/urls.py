"""Define padroes de URL para learning_logs."""

from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Pagina inicial
    path('', views.index, name='index'),

    # Mostra todos os assuntos
    path('topics', views.topics, name='topics'),

    # Pagina de detalhes para um unico assunto
    path('topics/<topic_id>\\d+)/', views.topic, name='topic'),
]
