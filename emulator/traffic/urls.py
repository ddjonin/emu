from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test_cases', views.test_cases),
    path('test_edit', views.test_edit),
    path('map', views.map),
    path('analysis', views.analysis),
    path('vehicles', views.vehicles),
    path('drivers', views.drivers),
    path('v2x_app', views.v2x_app),
    path('schedule', views.schedule),
    path('edit_route', views.edit_route),
    path('login', views.login),
]