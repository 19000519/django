from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic.base import HttpResponse, View, HttpResponse
from .forms import LoginForm, RegisterForm, NewVideoForm
from youtube.models import Video
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
class HomeView(View):
    template_name = 'Home.html'

    def get(self, request):
        variableA = 'some text here'
        return render(request, self.template_name, {'variableA' : variableA} )

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
           return HttpResponseRedirect('/')  
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
         #pass filled out HTML-form from view to LoginForm()
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')  
            else:
                return HttpResponseRedirect('/login')
        return HttpResponse('this is login view. POST request')

class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        if request.user.is_authenticated:
               return HttpResponseRedirect('/') 
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        #pass filled out HTML-form from view to RegisterForm()
        form = RegisterForm(request.POST)
        if form.is_valid():
            #Create a user account
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            new_user =User(username = username, password = password, email = email)
            new_user.set_password(password)
            new_user.save()
            return HttpResponseRedirect('/login')
        return HttpResponse()

class NewVideo(View):
    video_class = Video
    template_name = 'new_video.html'

    def get(self, request):
        form = NewVideoForm()
        return render(request, self.template_name, {'form' : form} )
    
    def post(self, request):
        return HttpResponse('This is Index view. POST Request.')