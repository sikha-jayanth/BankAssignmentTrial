import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator

from bankprojecttrial import settings
from .models import UserProfile,AccountInfo,Transactions,Transfer
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, View, ListView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import BalanceInfoForm,TransactionForm,TransferForm
# Create your views here.

class HomeMainView(View):
    def get(self,request):
        return render(request,'profiles/homemain.html')



class ProfileHomeView(LoginRequiredMixin,View):
    login_url = '/accounts/login/'
    template_name = 'profiles/profilehome.html'
    def get(self, request):
        context={}
        try:
            uid= UserProfile.objects.get(user=request.user).id
            print(uid,type(uid))
        except:
            uid=None

        context = {'uid': uid}
        return render(request, 'profiles/profilehome.html', context)



class AccountHomeView(View):
    template_name = 'profiles/accounthome.html'

    def get(self, request):
        context={}
        try:
            print(request.user)
            account= AccountInfo.objects.get(user=request.user)

        except:
            account=None
        context = {'account': account}
        return render(request, 'profiles/accounthome.html', context)





class CreateProfile(LoginRequiredMixin,CreateView):
    form_class = ProfileForm
    success_url = reverse_lazy('homemain')
    template_name = 'profiles/createprofile.html'

    def get_initial(self):
        return {'user': self.request.user}

def generate_message(request):
    return render(request,'profiles/success.html')

def activate_account(request):
    return render(request,'profiles/generatepinandaccno.html')


class EditProfile(LoginRequiredMixin,UpdateView):
    model=UserProfile
    fields = ['phone_no','Place','address']
    success_url = reverse_lazy('profilehome')
    template_name = 'profiles/editprofile.html'

class DeleteProfile(LoginRequiredMixin,DeleteView):
    model = UserProfile
    template="profiles/userprofile_confirm_delete.html"
    success_url = reverse_lazy('profilehome')

class ViewProfile(LoginRequiredMixin,DetailView):
    model = UserProfile
    fields="__all__"
    success_url = reverse_lazy('profilehome')
    template_name = "profiles/viewprofile.html"





def accno_gen():
    id=int(random.uniform(10000, 99999))
    return "SBB"+str(id)

def accpin_gen():
    return int(random.uniform(100000, 999999))

def generate_pin_accno(request):
    accno=accno_gen()
    accpin=accpin_gen()
    AccountInfo.objects.create(user=request.user,account_no=accno,account_pin=accpin)
    return render(request, "profiles/success.html")










class BalanceInfoView(LoginRequiredMixin,View):
    model=AccountInfo

    def post(self,request):
        form = BalanceInfoForm(request.POST)
        context={}
        if form.is_valid():
            pin = form.cleaned_data.get("pin")
            try:
                account = AccountInfo.objects.get(user=self.request.user,account_pin=pin)
                context["balance"] = account.balance

                return render(request, "profiles/BalanceInfo.html", context)
            except:
                context["form"] = form
                return render(request, "profiles/BalanceEnquiry.html", context)

        else:
            context["form"] = form
            return render(request, "profiles/BalanceEnquiry.html", context)

        return render(request, "profiles/BalanceEnquiry.html", context)

    def get(self,request):
        context={}
        form=BalanceInfoForm()
        context['form']=form
        return render(request,'profiles/BalanceEnquiry.html',context)


class TransactionsView(LoginRequiredMixin,FormView):
    form_class = TransactionForm
    fields="__all__"
    success_url = reverse_lazy('home')
    template_name = 'profiles/transactions.html'




    def get_initial(self):
        # print(self.request.user.map.account_no)
        return {'account_no': self.request.user}


    def post(self, request, *args, **kwargs):
        form = TransactionForm(request.POST)
        context = {}
        if form.is_valid():
            type = form.cleaned_data.get("type")
            amount=form.cleaned_data.get('amount')
            account_pin=form.cleaned_data.get('account_pin')
            # accno=form.cleaned_data.get("account_no")
            try:

                account = AccountInfo.objects.get(user=self.request.user,account_pin=account_pin)
                bal=account.balance
                if type=="credit":
                    bal=bal+amount
                elif type=="debit":
                    bal=bal-amount
                account.balance=bal
                account.save()
                form.save()
                return redirect('accounthome')
            except Exception as e:
                context["form"] = form
                return render(request, "profiles/transactions.html", context)
        else:
            context["form"]=form
            return render(request, "profiles/transactions.html", context)
        return render(request, "profiles/transactions.html", context)

class TransferView(LoginRequiredMixin,FormView):
    form_class = TransferForm
    success_url = reverse_lazy('home')
    template_name = 'profiles/transferamount.html'




    def get_initial(self):
        print(self.request.user.map.account_no)
        return {'from_account': self.request.user.map.account_no}


    def post(self, request, *args, **kwargs):
        form = TransferForm(request.POST)
        context = {}
        if form.is_valid():
            amount=form.cleaned_data.get('amount')
            to_account=form.cleaned_data.get('to_account')
            from_account=form.cleaned_data.get('from_account')
            account_pin=form.cleaned_data.get('account_pin')
            try:
                from_balance = AccountInfo.objects.get(user=self.request.user,account_pin=account_pin).balance
            # # to_balance = AccountInfo.objects.get(account_no=to_account).balance
            # print(type(amount), type(from_balance))

                from_balance = from_balance-amount
                to_account.balance += amount
                print(from_balance)
                print(to_account.balance)
                AccountInfo.objects.filter(account_no=from_account).update(balance=from_balance)
            # AccountInfo.objects.filter(account_no=to_account).update(balance=to_balance)
                to_account.save()
                form.save()
                return redirect('accounthome')
            except:
                context["form"] = form
                return render(request, "profiles/transferamount.html", context)


        else:
            context["form"]=form
            return render(request, "profiles/transferamount.html", context)

        return render(request, "profiles/transferamount.html", context)


class ActivityLog(ListView):
    model = Transactions
    template_name = "profiles/activitylog.html"

    def get_queryset(self):
        acno=self.request.user.map.account_no
        # qs=Transactions.objects.filter(account_no__account_no__contains=acno)
        # print(qs)
        return Transactions.objects.filter(account_no__account_no__contains=acno)


class TransferHistory(ListView):
    model=Transfer
    template_name='profiles/transferhistory.html'
    def get_queryset(self):
        acno=self.request.user.map.account_no
        return Transfer.objects.filter(from_account=acno)





