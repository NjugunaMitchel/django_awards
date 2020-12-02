from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import  CreateUserForm
from django.contrib import messages
from .models import Project,User
# Create your views here.

def login(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created for ' + User)
            return redirect('index')
        
    context ={'form':form}
    return render(request,'registration/login.html',context)

def signup(request):
    form=CreateUserForm()
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('landing')
    context = {'form':form}
    
    return render(request,'registration/login.html',context)

def landing(request):
   
    return render(request,'index.html')

def rates(request):
    project = Project.objects.all()
    obj=Project.objects.filter(rating=0).order_by('?').first()
    context={'project':project,'obj':obj}
    return render(request,'rates.html',context)