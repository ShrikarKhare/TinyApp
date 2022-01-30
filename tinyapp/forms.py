from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User, Url
from django.forms import ModelForm, TextInput

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        '''
        fields = '__all__'
        '''
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class UrlCreateForm(UserCreationForm):
    class Meta:
        model = Url

        fields = ['long_url']
class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class UrlModelForm(ModelForm):
    class Meta:
        model = Url
        fields = ['long_url']
        widgets = {
            'long_url': TextInput(attrs={'placeholder': 'https://', 'class': 'form-control bg-info'})
        }
