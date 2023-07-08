from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET']) #func based view define this decorator send api
def index(request):
    # all authors
    authors = Authors.objects.all()
    
    serializedAuthors = AuthorSerializer(authors, many=True) #do serialize fetch data , using many=True for our database have many data
    
    #all blogs
    blogs = Blog.objects.all()
    
    serializedBlogs = BlogSerializer(blogs, many=True)
    
    data = {
        'authors': serializedAuthors.data,
        'blogs': serializedBlogs.data
    }
    
    return Response(data)