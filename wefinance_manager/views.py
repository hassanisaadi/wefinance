from django.shortcuts import render, redirect
from .forms import AccountForm
from .models import Account

def account_create_view(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account-list')  # Redirect to another view after saving
    else:
        form = AccountForm()

    # Get all accounts to display in the list
    #accounts = Account.objects.all()

    return render(request, 'wefinance/account_form.html', {'form': form})


def account_list_view(request):
    accounts = Account.objects.all()  # Fetch all accounts
    return render(request, 'wefinance/account_list.html', {'accounts': accounts})
