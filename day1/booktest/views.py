# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo
from .models import HeroInfo

def index(request):
    list = BookInfo.objects.all()
    context = {'booklist':list}
    return render(request,'booktest/index.html',context)
