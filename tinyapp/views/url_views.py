from datetime import date
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.views.generic import CreateView, ListView,DetailView, DeleteView, UpdateView
from django.forms import ModelForm, TextInput
from tinyapp.models import User, Url
import random, string
from django.contrib.auth.mixins import LoginRequiredMixin

class URLListView(LoginRequiredMixin,ListView):
    model = Url
    context_object_name = 'urls'   # your own name for the list as a template variable
    # queryset = Url.objects.all()
    def get_queryset(self):
        
        current_user_id = self.request.user.id
        
        if current_user_id == None:
            return None
        
        return Url.objects.filter(user_id=current_user_id) 

    # current_user_id = self.request.user.id
    # queryset = User.objects.filter(pk = current_user_id)
    template_name = 'urls_index.html'  # Specify your own template name/location
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username') # Set cookie in the context object

        
        total_visits = str(context['url'])
        
        if self.request.session.get(total_visits) == None:
            context['total_visits'] = 0
        else:
            context['total_visits'] = self.request.session.get(total_visits)
        
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
    def get(self, request, short_url):                          
        long = Url.objects.values_list('long_url', flat = True).get(short_url = short_url)
        

        key = short_url

        if key in self.request.session.keys():
            self.request.session[key] += 1
        else:
            self.request.session[key] = 1

        print(self.request.session[key])
        return HttpResponseRedirect(long)

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
        # user = User.objects.first()
        current_user_id = self.request.user.id
        user = User.objects.filter(pk = current_user_id).first()
        form.instance.user = user
        form.instance.short_url = self.shortURLCreator()
        form.instance.date_created = date.today()
        
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')
        
        return context