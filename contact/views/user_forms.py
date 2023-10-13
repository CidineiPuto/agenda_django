from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "User registered.")
            return redirect("contact:login")
    return render(
        request,
        "contact/register.html",
        {"form": form},
    )


def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != "POST":
        return render(
            request,
            "contact/register.html",
            {
                "form": form,
            },
        )

    form = RegisterUpdateForm(
        instance=request.user,
        data=request.POST,
    )

    if not form.is_valid():
        return render(
            request,
            "contact/register.html",
            {
                "form": form,
            },
        )

    form.save()
    return render(
        request,
        "contact/register.html",
        {
            "form": form,
        },
    )


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            messages.success(request, "Logged in successfully")
            auth.login(request, user)
            return redirect("contact:index")
        messages.error(request, "Invalid login")
    return render(
        request,
        "contact/login.html",
        {
            "form": form,
        },
    )


def logout_view(request):
    auth.logout(request)
    return redirect("contact:login")
