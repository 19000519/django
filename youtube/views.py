from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View, HttpResponse
from .forms import LoginForm

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
        return render(request, self.template_name, {'form' : form})


    def post(self, request):
        print('HELLO THIS POST')
        return HttpResponse('This is Index view. POST Request.')


class NewVideo(View):
    template_name = 'new_video.html'

    def get(self, request):
        variableA = 'New Video'
        return render(request, self.template_name, {'variableA' : variableA} )
    
    def post(self, request):
        return HttpResponse('This is Index view. POST Request.')