from django.urls import path
from . import views
from django_app.views import InfoView

app_name = 'django_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('info/', InfoView.as_view(), name='info')
]


