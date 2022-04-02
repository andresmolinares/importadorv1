from django.urls import path

from pruebas import views

urlpatterns = [
    path('', views.importer, name='index'),
]