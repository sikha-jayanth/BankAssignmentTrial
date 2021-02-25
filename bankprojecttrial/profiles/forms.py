from django import forms
from django.forms import ModelForm
from django.views.generic import ListView

from .models import UserProfile,AccountInfo,Transactions,Transfer

class ProfileForm(ModelForm):

    class Meta:
        model=UserProfile
        fields="__all__"
        widgets = {
            "user": forms.HiddenInput(),

        }



class BalanceInfoForm(forms.Form):
    pin=forms.IntegerField(widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        pin = cleaned_data.get("pin")
        try:
            object=AccountInfo.objects.get(account_pin=pin)
        except:
            msg = "invalid pin"
            self.add_error("pin", msg)




class TransactionForm(ModelForm):
    account_pin = forms.IntegerField(widget=forms.PasswordInput)
    class Meta:
        model=Transactions
        fields=['account_no','amount','type']
        widgets={
            'account_no':forms.HiddenInput(),
            'type':forms.Select(),
            # "account_pin": forms.PasswordInput(attrs={'class': "form-control"})
        }



    def clean(self):
        cleaned_data = super().clean()
        pin = cleaned_data.get("account_pin")
        amount = cleaned_data.get("amount")
        try:
            object = AccountInfo.objects.get(account_pin=pin)
            if (object.balance < amount):
                msg = "insufficent amount"
                self.add_error("amount", msg)

        except:
            msg = "you have provided invalid pin"
            self.add_error("account_pin", msg)



class TransferForm(ModelForm):
    account_pin=forms.IntegerField(widget=forms.PasswordInput)
    class Meta:
        model=Transfer
        fields=['from_account','to_account','amount']
        widgets={
            "from_account": forms.TextInput(attrs={'class': "form-control",'readonly':True}),
            "amount":forms.NumberInput(attrs={'class': "form-control"}),
            # "account_pin":forms.PasswordInput(attrs={'class': "form-control"})

        }
    def clean(self):
        cleaned_data=super().clean()
        amount= cleaned_data.get('amount')
        pin=cleaned_data.get('account_pin')
        to_account_no=cleaned_data.get('to_account')
        from_account_no = cleaned_data.get('from_account')
        if to_account_no.account_no == from_account_no:
            msg="you cant transfer to your own account"
            self.add_error('to_account', msg)
        try:
            object = AccountInfo.objects.get(account_pin=pin)
            if (object.balance < amount):
                msg = "insufficent amount"
                self.add_error("amount", msg)

        except:
            msg = "you have provided invalid pin"
            self.add_error("account_pin", msg)










