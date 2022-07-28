from django.conf import settings

from multiprocessing import context
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
from django.contrib import auth
from django.contrib import messages
from .models import Feature, newFeatures, Post

# Create your views here.

def index(request):
    features = Feature.objects.all()
    posts = Post.objects.all()
    return render(request, 'index.html', {'features': features, 'posts': posts})


def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html', {'posts': posts})

def signup(request):
    return render(request, 'signup.html')

def create_user(request):
   if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        signup_as = request.POST['select_as']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Exists')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, signup_as=signup_as)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password doesnot matches')
            return redirect('signup')


def login(request):
     return render(request, 'login.html')

def login_auth(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        signup_as = request.POST['signup_as']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if(signup_as == 1):
                return redirect('studentdashboard')
            else:
                return redirect('index')
        else:
            messages.info(request, 'Credentials are invalid')
            return redirect('login')

def studentdashboard(request):
    return render(request, 'studentdashboard.html')


def studentprofile(request):
    return render(request, 'student-profile.html')
