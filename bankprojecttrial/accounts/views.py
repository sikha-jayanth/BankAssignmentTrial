from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, CreateView, FormView, View
from profiles.models import UserProfile,AccountInfo
from .forms import CreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm


# Create your views here.
class SignUpView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'





class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html', {'form': AuthenticationForm()})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))

            if user is None:
                return render(request, 'accounts/login.html', {'form': form, 'invalid_creds': True})

            login(request, user)
            return redirect('homemain')
        return render(request, 'accounts/login.html', {'form': form, 'invalid_creds': True})


def logout_view(request):
    logout(request)
    return redirect('login')





class HomeView(LoginRequiredMixin,View):
    login_url = '/accounts/login/'
    template_name = 'accounts/home.html'
    def get(self, request):
        context={}
        try:
            uid= UserProfile.objects.get(user=request.user).id
            print(uid,type(uid))
        except:
            uid=None

        context = {'uid': uid}
        return render(request, 'accounts/home.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            auth.logout(request)
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/reset_password.html', {
        'form': form
    })

class AccountHomeView(View):
    template_name = 'accounts/accounthome.html'

    def get(self, request):
        context={}
        try:
            print(request.user)
            account= AccountInfo.objects.get(user=request.user)

        except:
            account=None
        context = {'account': account}
        return render(request, 'accounts/accounthome.html', context)

class HomeMainView(View):
    def get(self,request):
        return render(request,'accounts/homemain.html')


