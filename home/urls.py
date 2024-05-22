from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.index, name='home'),
    path("vision/", views.vision, name='vision'),
    path("mission/", views.mission, name='mission'),
    path("revenue/", views.revenue, name='revenue'),
    path("more", views.more, name='more'),
]