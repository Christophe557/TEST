"""projet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from appli import views

#---- activation en prod ------------
from django.views.static import serve
#-----------------------------------



urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^appli/', include('appli.urls', namespace='appli')),

#---- activation en prod pour servir fichiers STATIC ------------
#---- en dév (serveur local Django) quand DEBUG=False -----------
#---- et lancer ./manage.py runserver --insecure ----------------
   re_path(r'^static/(?P<path>.*)$', serve,{'document_root':settings.STATIC_ROOT}),
#-----------------------------------

]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
            re_path(r'^__debug__/', include(debug_toolbar.urls)),
            ] + urlpatterns
