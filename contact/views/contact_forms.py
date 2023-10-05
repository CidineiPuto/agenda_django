from typing import Any

from django import forms
from django.core.exceptions import ValidationError
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

    def clean(self) -> dict[str, Any]:
        cleaned_data = self.cleaned_data
        self.add_error("first_name", ValidationError("Mensagem", code="invalid"))
        return super().clean()


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
