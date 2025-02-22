

from django.urls import path, include # type: ignore
from . import views as blog_views


urlpatterns = [
    path('', blog_views.index),
]
