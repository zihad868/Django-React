from . views import ProjectView
from rest_framework import routers
from django.urls import path, include

route = routers.DefaultRouter()

route.register("", ProjectView, basename="projectview")

urlpatterns = [
    path("api/", include(route.urls))
]