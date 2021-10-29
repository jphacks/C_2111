from django.urls import path
from . import views

app_name = 'django_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('info/', views.info, name='info')
]
