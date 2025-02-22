
from django.urls import path # type: ignore
from . import views as home_views


urlpatterns = [
    path('',home_views.index),
]
