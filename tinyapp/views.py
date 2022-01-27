from re import template
from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import ListView
from django.forms import ModelForm, TextInput
from .models import User
from .models import Url
from .forms import UserRegisterForm
import random, string
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

class UrlModelForm(ModelForm):
    class Meta:
        model = Url
        fields = ['long_url']
        widgets = {
            'long_url': TextInput(attrs={'placeholder': 'http://'})
        }
            

class UrlCreateView(CreateView):
    form_class = UrlModelForm
    success_url = '/urls/'
    template_name = 'urls_new.html'
    def shortURLCreator(self):
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return x
    def form_valid(self, form):
        user = User
        form.instance.user = user
        form.instance.short_url = self.shortURLCreator()
        return super().form_valid(form)