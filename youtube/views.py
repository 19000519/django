
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.generic.base import HttpResponse, View 
from .forms import LoginForm, RegisterForm
from youtube.models import Video

# Create your views here.
class HomeView(View):
    template_name = 'Home.html'

    def get(self, request):
        variableA = 'some text here'
        return render(request, self.template_name, {'variableA' : variableA} )

class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print('HELLO THIS POST')
        return HttpResponse('this is login view. POST request')

class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        #pass filled out HTML-form from view to RegisterForm()
        form = RegisterForm(request.POST)
        if form.is_valid():
            #Create a user account
             return HttpResponseRedirect('/thanks/')
        return HttpResponse('this is register view. POST request')

class NewVideo(View):
    video_class = Video
    template_name = 'new_video.html'

    def get(self, request):
        variableA = 'New Video'
        return render(request, self.template_name, {'variableA' : variableA} )
    
    def post(self, request):
        return HttpResponse('This is Index view. POST Request.')