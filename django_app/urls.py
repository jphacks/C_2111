from django.urls import path
from . import views
from django_app.views import SampleTemplateView

app_name = 'django_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('info/', SampleTemplateView.as_view(), name='info')
]
