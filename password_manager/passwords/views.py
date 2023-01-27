from django.shortcuts import render, redirect
from .models import UserPW
from .forms import PasswordForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


@login_required(login_url="login")
def home(request):
    passwords = UserPW.objects.filter(user=request.user)
    context = {'passwords': passwords}
    return render(request, 'passwords/home.html', context)


@login_required(login_url="login")
def createPassword(request):
    page = 'create'
    form = PasswordForm()
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid:
            user_pw = form.save(commit=False)
            if user_pw.domain is not None and user_pw.pwd is not None:
                user_pw.user = request.user
                user_pw.save()
                form.save()
                return redirect('home')
            else:
                messages.success(request, "Please fill all the fields!")

    context = {'form': form, 'page': page}
    return render(request, 'passwords/password_form.html', context)


@login_required(login_url="login")
def updatePassword(request, pk):
    page = 'update'
    password = UserPW.objects.get(id=pk)
    form = PasswordForm(instance=password)
    if request.method == 'POST':
        form = PasswordForm(request.POST, instance=password)
        if form.is_valid:
            form.save()
            return redirect('home')
    context = {'form': form, 'page': page}
    return render(request, 'passwords/password_form.html', context)


@login_required(login_url="login")
def deletePassword(request, pk):
    page = 'delete'
    password = UserPW.objects.get(id=pk)
    form = PasswordForm(instance=password)
    if request.method == 'POST':
        password.delete()
        return redirect('home')
    context = {'form': form, 'page': page}
    return render(request, 'passwords/password_form.html', context)
