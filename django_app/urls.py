from django.urls import path
from . import views

app_name = 'django_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('questionnaires/', views.questionnaires, name='questionnaires'),
    path('<uuid:questionnaire_id>/info/', views.info, name='info'),
    path('<uuid:questionnaire_id>/new/', views.new, name='new'),
]
