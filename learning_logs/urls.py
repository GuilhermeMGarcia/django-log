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

    # Pagina para adicionar um novo assunto
    path('new_topic/', views.new_topic, name='new_topic'),

    # Pagina para adicionar uma nova entrada
    path('new_entry/<topic_id>\\d+)/', views.new_entry, name='new_entry'),

]
