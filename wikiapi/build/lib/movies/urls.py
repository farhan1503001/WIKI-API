from django.urls import path
from django.urls.conf import include
from . import views
from rest_framework import routers

route=routers.DefaultRouter()
route.register('Movies',views.Movie_view)
urlpatterns = [
   path('',include(route.urls)),
]
