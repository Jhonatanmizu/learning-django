

from django.urls import path, include # type: ignore
from . import views as blog_views

app_name = 'blog'

urlpatterns = [
    path('', blog_views.index,name="blog"),
    path('post/<int:id>/', blog_views.post,name="post"),
]
