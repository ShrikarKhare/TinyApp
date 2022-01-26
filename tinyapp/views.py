from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from .models import User
from .models import Url
from .forms import UserRegisterForm
# Create your views here.

class UserRegistrationView(CreateView):
    form_class = UserRegisterForm
    success_url = '/register'
    template_name = 'register.html'
class URLListView(ListView):
    model = Url
    context_object_name = 'urls'   # your own name for the list as a template variable
    queryset = [{'short_url': 'b2xVn2', 'long_url': 'https://www.google.com'}] # Get 5 books containing the title war
    template_name = 'urls_index.html'  # Specify your own template name/location