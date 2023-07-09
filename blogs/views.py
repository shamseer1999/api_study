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

@api_view(['GET','POST'])
def addAuthor(request):
    authors = Authors.objects.all()
    serializedAuthors = AuthorSerializer(authors, many=True)
    
    if request.method == 'POST':
        serializedAuthorsData = AuthorSerializer(data=request.data)
        
        if serializedAuthorsData.is_valid():
            serializedAuthorsData.save()
            out = {
                'message':'author created successfully',
                'status':1,
                'errors':{}
            }
        else:
            out = {
                'message':'author creation failed',
                'status':0,
                'errors':serializedAuthorsData.errors
            }
        
        return Response(out)
    
    data = {
        'authors':serializedAuthors.data
    }
    return Response(data)

@api_view(['GET','POST'])
def addBlog(request):
    blogs = Blog.objects.all()
    
    serializedBlogs = BlogSerializer(blogs, many=True)
    
    if request.method =='POST':
        # print("mmmm",request.data['author'])
        author = Authors.objects.get(pk = request.data['author'])
        # print(type(author))
        if author is not None:
            request.data['author'] = author.id
            serializedBlogs = BlogSerializer(data=request.data)
            
            if serializedBlogs.is_valid():
                serializedBlogs.save()
                out = {
                    'message':'Your blog saved successfully',
                    'status':1,
                    'errors':{}
                }
            else:
                out = {
                    'message':'something went wrong',
                    'status':0,
                    'errors':serializedBlogs.errors
                }
        else:
            out = {
                'message':'Author does not exist',
                'status':0,
                'errors':{}
            }
        return Response(out)
    
    data = {
        'blogs':serializedBlogs.data
    }
    
    return Response(data)