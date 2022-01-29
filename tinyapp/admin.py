from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import User, Url

admin.site.register(User, UserAdmin)
admin.site.register(Url)
admin.site.site_header = 'TinyApp Administration'