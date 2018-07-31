from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('maps/', views.route, name='route'),
    path('s', views.ind, name='hom'),
]
