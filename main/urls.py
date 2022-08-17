from django.urls import path
from .views import HomeView, register
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(HomeView.as_view()),name='home'),
    path('aboutus', login_required(views.about_usView), name='about'),
    path('accounts/register', register, name='register')
]