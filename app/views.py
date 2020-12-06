from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import  RatesForm
from django.views.generic import CreateView
from django.contrib import messages
from .models import Project,Profiles,Reviews
# Create your views here.

def landing(request):
   
    return render(request,'index.html')


def rates(request):
    project = Project.objects.all()
    obj=Project.objects.filter(reviews=1).order_by('?').first()
    context={'project':project,'obj':obj}
    return render(request,'rates.html',context)

    

def rateform(request):
    form = RatesForm()
    return render(request,'rateform.html',{'form': form})

def newproject(request):

    return render(request,'newproject.html')