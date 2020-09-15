from django.shortcuts import render, redirect, Http404
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as _login
from django.contrib.auth import logout as _logout
from django.conf import settings

from appointment.forms.authentication import LoginForm, RegisterForm
from appointment.forms.profile import DoctorForm


REGISTRATION_TYPE_DOCTOR = 'doctor'
REGISTRATION_TYPE_PATIENT = 'patient'


def login(request):
    """
    Login a User and return a page
    :param request:
    :return:
    """

    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST.get("email")
        password = request.POST.get("password")
        if form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                _login(request, user)
                return redirect("home_page")
        else:
            messages.error(request, "Invalid Email or Password")
            return redirect("login")

    template = "authentication/login.html"
    form = LoginForm()
    context = {
        "form": form
    }
    return render(request, template, context)


def logout(request):
    """
    Log user out and return the homepage
    :param request:
    :return:
    """
    _logout(request)
    return redirect("home_page")


def register(request):
    """
    Register a user and return the profile page
    :param request:
    :return:
    """
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get("username")
            user.set_password(form.cleaned_data.get("password"))
            user.save()

            registration_type = request.POST.get("registration_type")
            if registration_type == REGISTRATION_TYPE_DOCTOR:
                profile_form = DoctorForm({"user": user, "country": "GH"})
            # import pdb; pdb.set_trace()
            if profile_form.is_valid():
                profile_form.save()
            else:
                import pdb; pdb.set_trace()
            return redirect("home_page")

    template = "authentication/register.html"
    form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, template, context)


