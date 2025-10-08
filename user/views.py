from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def product(request):
    mydict={}
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mobile')
        d=request.POST.get('city')
        e=request.POST.get('address')
        f=request.POST.get('landmark')
        g=request.POST.get('OS')
        tbl_orderlist(Name=a,Email=b,Mobile=c,City=d,Address=e,NL=f,OS=g).save()
        return HttpResponse("<script>alert('order confirmed');location.href='/product' </script>")

    return render(request,'product.html',mydict)
def contact(request):
    return render(request,'contact.html')