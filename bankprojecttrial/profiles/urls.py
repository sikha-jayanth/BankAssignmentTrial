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
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import HomeMainView,ProfileHomeView,AccountHomeView, CreateProfile, EditProfile, DeleteProfile, ViewProfile, \
    generate_pin_accno, generate_message, activate_account, BalanceInfoView, TransactionsView, TransferView, \
    ActivityLog, TransferHistory

urlpatterns = [
    path('homemain', HomeMainView.as_view(), name='homemain'),
    path('accounthome', AccountHomeView.as_view(), name='accounthome'),
    path('profilehome', ProfileHomeView.as_view(), name='profilehome'),
    path('createprofile', CreateProfile.as_view(), name='createprofile'),
    path('viewprofile<int:pk>', login_required(ViewProfile.as_view()), name='viewprofile'),
    path('editprofile/<int:pk>/', EditProfile.as_view(), name='editprofile'),
    path('deleteprofile<int:pk>', DeleteProfile.as_view(), name='deleteprofile'),
    path('activate', activate_account, name='activate'),
    path('generate', generate_pin_accno, name='generate'),
    path('generatemessage', generate_message, name='generatemessage'),
    path('balanceinfo', BalanceInfoView.as_view(), name='balanceinfo'),
    path('transactions', TransactionsView.as_view(), name='transactions'),
    path('transfer', TransferView.as_view(), name='transfer'),
    path('activitylog', ActivityLog.as_view(), name='activitylog'),
    path('transferhistory', TransferHistory.as_view(), name='transferhistory')

]
