from django.shortcuts import render # type: ignore
from django.http import HttpResponse,HttpRequest, Http404 # type: ignore
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


def post(request:HttpRequest,id:int):
  target_post:dict[str,Any] | None = None
  for post in posts:
    if post["id"] == int(id):
      target_post = post
      break

  
  if target_post is None:
    raise Http404("Post not found")

  context={
    "document_title":"Blog",
    "title":f'Blog Post {target_post["title"]}',
    "description":f'{target_post["body"]}',
    "post":target_post,
  }
  return render(request, 'blog/post.html',context) 