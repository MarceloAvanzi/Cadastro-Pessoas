import imp
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

class HomeView(TemplateView):
    template_name = 'main/index.html'

def about_usView(request):
    template_aboutus = 'main/aboutus.html'
    return render(request, template_aboutus)