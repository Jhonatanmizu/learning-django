from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from .data import posts

# Create your views here.
def index(request):
  context={
    "document_title":"Blog",
    "title":"Blog Page",
    "description":"This is the blog page",
    "posts":posts
  }
  return render(request, 'blog/index.html',context)
