from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    
    data = {
        'all_blogs':list(blogs.values())
    }
    return JsonResponse(data)