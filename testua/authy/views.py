from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm


# Create your views here.
def login_page(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'authy/login_registry.html', {'page': page})


def registry_page(request):
    page = 'registry'
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            user = authenticate(request, username=user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return redirect('home')
    context = {'form': form, 'page': page}
    return render(request, 'authy/login_registry.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')