from django.core.paginator import Paginator  # type: ignore
from django.db.models import Q  # type: ignore
from django.shortcuts import get_object_or_404  # type: ignore
from django.shortcuts import redirect, render  # type: ignore

from contact.models import Contact


def create(request):
    context = {}
    return render(
        request,
        "contact/create.html",
        context,
    )
