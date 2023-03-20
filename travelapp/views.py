from django.shortcuts import render
from .models import place

# Create your views here.
def fun(request):
    obj=place.objects.all()
    return render(request,"index.html",{'results':obj})
def detail(request,place_id):
    obj1=place.objects.get(id=place_id)
    return render(request,'detail.html',{'result':obj1})
