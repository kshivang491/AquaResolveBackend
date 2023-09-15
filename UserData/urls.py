from django.contrib import admin
from django.urls import path,include
from UserData.views import UserViewSet, UserProblemViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userproblems', UserProblemViewSet)

urlpatterns = [
    path('',include(router.urls))
]
