from django.urls import path
from . import views

app_name = 'academic'

urlpatterns = [
    path('', views.cards, name='cards'),
]
