from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.
def index(request):
    context = {
        "document_title":"Home",
        "title":"Home Page",
    }
    return render(request,'home/index.html',context)
  

    