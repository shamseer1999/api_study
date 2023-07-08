from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
# Create your views here.
def index(request):
    data = {
        'test':'hello world'
    }
    return JsonResponse(data)