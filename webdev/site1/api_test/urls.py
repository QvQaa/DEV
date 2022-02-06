from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from api_test.views import MovieViewSet
from django.urls import path

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)

urlpatterns = [
    path('', MovieViewSet, name='index'),
]
