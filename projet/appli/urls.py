from django.urls import path, re_path
from . import views

app_name = 'appli'

urlpatterns = [
    re_path(r'^citations/$', views.citations, name='citations'),
    re_path(r'^citez/$', views.citez, name='citez'),
    re_path(r'^apropos/$', views.apropos, name='apropos'),
]

