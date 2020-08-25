from django.shortcuts import render, HttpResponseRedirect, reverse

from myuser.models import MyUser
from myuser.forms import LoginForm, CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from customuser.settings import AUTH_USER_MODEL

# Create your views here.
@login_required
def index_view(request):
    return render(request, "index.html", {"model": AUTH_USER_MODEL})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("homepage"))
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))

def signup_view(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = MyUser.objects.create_user(
                display_name = data.get("display_name"),
                username = data.get("username"),
                password = data.get("password"),
            )
            
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))
    form = CreateUserForm()
    return render(request, "generic_form.html", {"form": form})