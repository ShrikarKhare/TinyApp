from datetime import date
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import CreateView, ListView,DetailView, DeleteView, UpdateView
from django.forms import ModelForm, TextInput
from tinyapp.models import User, Url
import random, string
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify

class URLListView(LoginRequiredMixin,ListView):
    model = Url
    context_object_name = 'urls'   
    def get_queryset(self):
        
        current_user_id = self.request.user.id
        
        if current_user_id == None:
            return None
        
        return Url.objects.filter(user_id=current_user_id) 

    template_name = 'urls_index.html'  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')

        return context

class UrlModelForm(ModelForm):
    class Meta:
        model = Url
        fields = ['long_url']
        widgets = {
            'long_url': TextInput(attrs={'placeholder': 'http://'})
        }
class UrlDeleteView(DeleteView):
    model = Url
    success_url = '/urls'

class UrlUpdateView(UpdateView):
    model = Url 
    success_url = '/urls'
    fields = ['long_url']
    template_name = 'urls_detail.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username') 
        cookie_id = str(context['url']) 
        
        if self.request.COOKIES.get(cookie_id) == None:
            context['total_visits'] = 0 
        else:
            context['total_visits'] = self.request.COOKIES.get(cookie_id)
            
        if self.request.COOKIES.get(cookie_id + 'unique_visits') == None:
            context['unique_visits'] = 0 
        else:
            context['unique_visits'] = self.request.COOKIES.get(cookie_id + 'unique_visits')
        
        return context


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        
        current_user = self.request.session.get('username')
        
        current_user_id = None
        
        if current_user:
            current_user_id = User.objects.filter(username=current_user)[0].id

        if(self.object.user_id != current_user_id):
            return HttpResponseForbidden()
        
        return super().get(request, *args, **kwargs)


class UrlRedirectView(DetailView):
    def count_unique_ids(self):
        count = 0
        if self.request.session.get('username') == None:
            count += 1

        return count
        
    def get(self, request, short_url):                          
        
        self.short_url = short_url
             
        url_obj = Url.objects.filter(short_url=short_url)
        
        response = HttpResponseRedirect(url_obj[0].long_url)
        
        cookie_id = short_url 
        
        
        if cookie_id in request.COOKIES.keys():
            counter =  int(request.COOKIES[cookie_id]) + 1
            response.set_cookie(cookie_id, counter)   
        else:
            response.set_cookie(cookie_id, 1)
                                  
        cookie_id = short_url + "unique_visits" 

        if self.request.session.get('username') == None:

            if cookie_id in request.COOKIES.keys():
                count = int(request.COOKIES[cookie_id]) + 1
                response.set_cookie(cookie_id, count)
            else:
                response.set_cookie(cookie_id, 1)
        else:
            if cookie_id in request.COOKIES.keys():
                response.set_cookie(cookie_id, request.COOKIES[cookie_id])
            else:
                response.set_cookie(cookie_id, 1)
            
        return response


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')
        return context

class UrlCreateView(CreateView):
    
    form_class = UrlModelForm
    success_url = '/urls'
    template_name = 'urls_new.html'
    
    def shortURLCreator(self):
        x = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return x
    
    def form_valid(self, form):
        current_user_id = self.request.user.id
        user = User.objects.filter(pk = current_user_id).first()
        form.instance.user = user
        form.instance.short_url = self.shortURLCreator()
        form.instance.date_created = date.today()
        # form.instance.slug_field = slugify(form.instance.long_url)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')

        return context
    