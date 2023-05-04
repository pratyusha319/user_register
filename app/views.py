from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
from app.models import *
def registration(request):
    UFO=userform()
    PFO=profileform()
    d={'UFO':UFO,'PFO':PFO}
    if request.method=='POST' and request.FILES:
        UFD=userform(request.POST)
        PFD=profileform(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            NSUO=UFD.save(commit=False)
            NSUO.set_password(UFD.cleaned_data['password'])
            NSUO.save()
            NSPO=PFD.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()
            return HttpResponse('data inserted successfully')
        else:
            return HttpResponse('data not inserted successfully')
    return render(request,'registration.html',d)