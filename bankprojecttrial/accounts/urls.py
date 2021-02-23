"""bankprojecttrial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import SignUpView, LoginView, HomeView, change_password,HomeMainView,AccountHomeView,logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout',logout_view,name='logout'),
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),name="password_reset_confirm"),
    path("password-reset-complete/",auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),name="password_reset_complete"),
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('home', HomeView.as_view(), name='home'),
    path('change_password', change_password, name='change_password'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('homemain',HomeMainView.as_view(),name='homemain'),
    path('accounthome',AccountHomeView.as_view(),name='accounthome'),

]
