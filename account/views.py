from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import CreateView, UpdateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class LoginInterface(LoginView):
    template_name = 'login.html'
    
class LogoutClass(LogoutView):
    template_name = 'logout.html'

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name= 'signup.html'
    success_url = '/account/login'

    def get(self, request, *args, **kwrgs):
        if (self.request.user.is_authenticated):
            return redirect('home')
        return super().get(self, request, *args, **kwrgs)
    
