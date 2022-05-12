from django.shortcuts import render,HttpResponse,redirect
from apps.models import Wallpaper
# Create your views here.
def index(request):
  wp = Wallpaper.objects.all()
  return render(request,'index.html',{'wp':wp})
def viewimg(request,imagen):
  wp = Wallpaper.objects.filter(id=imagen)[:1].get()
  return render(request,'viewimg.html',{'wp':wp})