from django import forms
from django.core.paginator import Paginator  # type: ignore
from django.db.models import Q  # type: ignore
from django.shortcuts import get_object_or_404  # type: ignore
from django.shortcuts import redirect, render  # type: ignore

from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            "first_name",
            "last_name",
            "phone",
        )


def create(request):
    if request.method == "POST":
        context = {"form": ContactForm(data=request.POST)}

        return render(
            request,
            "contact/create.html",
            context,
        )
    context = {"form": ContactForm()}
    return render(
        request,
        "contact/create.html",
        context,
    )
