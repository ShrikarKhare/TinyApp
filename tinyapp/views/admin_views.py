from django.views.generic import ListView
from ..models import User
from django.contrib.auth.mixins import PermissionRequiredMixin

class SeeAdminsView(PermissionRequiredMixin, ListView):
    model = User
    context_object_name = 'users'
    template_name = 'admin.html'
    permission_required = 'tinyapp.view_user'

    def get_queryset(self):
        current_user = self.request.user.id 
        if current_user == None or self.request.user.has_perm('tinyapp.view_user') == False:
            return None
        return User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.session.get('username')
        return context