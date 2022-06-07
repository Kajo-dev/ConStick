import re
from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from dayplan.models import Plans
from .forms import PlansFrom
# Create your views here.

def home_view_dodawanie(request,*args,**kwargs):
    form = PlansFrom(request.POST or None)
    if form.is_valid():
        form.save()
    context={
        "form": form
    }
    return render(request,'plany.html',context)

def home_view(request,*args,**kwargs):
    obj = Plans.objects.get(id=1)
    context={
        "obiekt": obj
    }
    return render(request,'index.html',context)

