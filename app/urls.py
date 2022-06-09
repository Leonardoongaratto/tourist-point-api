"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from attractions.api.viewsets import AtracaoViewSet
from address.api.viewsets import EnderecoViewSet
from comments.api.viewsets import ComentarioViewSet
from evaluation.api.viewsets import AvaliacaoViewSet

router = routers.DefaultRouter()
router.register(r'points', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'attractions', AtracaoViewSet)
router.register(r'address', EnderecoViewSet)
router.register(r'comments', ComentarioViewSet)
router.register(r'evaluations', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
